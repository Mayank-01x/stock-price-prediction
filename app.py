from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import yfinance as yf
import os
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

if not os.path.exists('static'):
    os.makedirs('static')

def predict_stock(ticker, start_date, end_date, days):
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            return None, None, None, "No data found for the given ticker or dates."

        df = df[['Close']].dropna()
        df['Prediction'] = df[['Close']].shift(-days)

        X = np.array(df.drop(['Prediction'], axis=1))[:-days]
        y = np.array(df['Prediction'])[:-days]

        if len(X) < 60:
            return None, None, None, "Not enough data to train the model."

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, predictions))

        # Prepare date indexes
        full_index = df.index[:-days]
        test_len = len(y_test)
        test_dates = full_index[-test_len:]

        # Future prediction
        future_X = np.array(df.drop(['Prediction'], axis=1))[-days:]
        future_predictions = model.predict(future_X)
        future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=days)

        # Plotly visualization
        trace_actual = go.Scatter(x=test_dates, y=y_test, mode='lines', name='Actual Price', line=dict(color='blue'))
        trace_predicted = go.Scatter(x=test_dates, y=predictions, mode='lines', name='Predicted (Test)', line=dict(color='orange', dash='dot'))
        trace_future = go.Scatter(x=future_dates, y=future_predictions, mode='lines+markers', name=f'Future {days}-Day Forecast', line=dict(color='green'))

        layout = go.Layout(
            title=f'{ticker.upper()} Stock Price Forecast',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Price'),
            hovermode='closest'
        )

        fig = go.Figure(data=[trace_actual, trace_predicted, trace_future], layout=layout)
        pyo.plot(fig, filename='static/interactive_plot.html', auto_open=False)

        prediction_table = list(zip(future_dates.strftime('%Y-%m-%d'), future_predictions.round(2)))
        return rmse, prediction_table, df[['Close']], None

    except Exception as e:
        return None, None, None, f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker = 'AAPL'
    start_date = '2015-01-01'
    end_date = '2024-01-01'
    days = 30
    rmse = None
    prediction_table = []
    error = None

    if request.method == 'POST':
        ticker = request.form['ticker'].strip().upper()
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        try:
            days = int(request.form['days'])
        except:
            error = "Invalid number of prediction days."
        else:
            rmse, prediction_table, close_data, error = predict_stock(ticker, start_date, end_date, days)

    return render_template('index.html', ticker=ticker, start_date=start_date,
                           end_date=end_date, days=days, rmse=rmse,
                           predictions=prediction_table, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

