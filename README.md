
[![GitHub Repo](https://img.shields.io/badge/GitHub-Mayank--01x%2Fstock--price--prediction-blue?logo=github)](https://github.com/Mayank-01x/stock-price-prediction)
[![Live on Render](https://img.shields.io/badge/Live-Demo-success?logo=render)](https://stock-price-prediction-cyrf.onrender.com)

# 📈 Stock Price Prediction Web App

This is an interactive stock price prediction web application built with **Flask**, **scikit-learn**, and **Plotly**. It allows users to select or search global stock symbols, choose a historical date range, and predict future stock prices using a machine learning model.

---

## 🚀 Features

- 🔎 Autocomplete stock symbol input (supports global stocks like `AAPL`, `TSLA`, `RELIANCE.NS`, `BTC-USD`)
- 📅 Select custom start & end dates for historical training
- ⏳ Choose custom future prediction range (days)
- 📊 Interactive Plotly charts (actual, predicted, and future prices)
- 📥 Prediction output table
- ☁️ Deployable to **Render** or **Heroku**

---

## 🛠 Tech Stack

- Python 3.x
- Flask (Web Framework)
- scikit-learn (Linear Regression model)
- yfinance (Stock data)
- Plotly (Interactive graphs)
- HTML/CSS/JS (Frontend)

---

## 🔧 Project Structure

```
stock-price-prediction/
├── app.py                  # Flask server
├── templates/
│   └── index.html          # Main frontend
├── static/
│   └── interactive_plot.html (auto-generated)
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config (optional)
└── README.md               # Project documentation
```

---

## 📦 Installation (Local)

```bash
git clone https://github.com/Mayank-01x/stock-price-prediction.git
cd stock-price-prediction
pip install -r requirements.txt
python app.py
```

Then visit: [http://localhost:10000](http://localhost:10000)

---

## 🌐 Deployment (Render)

1. Push your project to GitHub
2. Create a new **Web Service** at [https://render.com](https://render.com)
3. Use these settings:
   - Environment: Python
   - Start Command: `gunicorn app:app`
   - Build Command: *(leave blank)*
4. Done! 🎉

---

## 🙋 Author

**Mayank Aggarwal**  
GitHub: [@Mayank-01x](https://github.com/Mayank-01x/Object-Detection)

---

## 📄 License

This project is licensed under the **MIT License**.
