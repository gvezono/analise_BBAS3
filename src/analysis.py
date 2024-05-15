import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker):
    stock = yf.Ticker(f"{ticker}.SA")
    hist = stock.history(period="3mo")  # Carrega dados dos últimos três meses para garantir cobertura suficiente
    return hist['Close'].tail(60)  # Seleciona apenas os últimos 60 dias úteis

def calculate_rsi(data, window=14):
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_stochastic_oscillator(data, window=14):
    low_min = data.rolling(window=window).min()
    high_max = data.rolling(window=window).max()
    k = 100 * (data - low_min) / (high_max - low_min)
    return k

def check_buy_conditions(data, ticker):
    rsi = calculate_rsi(data)
    stochastic = calculate_stochastic_oscillator(data)
    moving_average = data.rolling(window=20).mean()
    std_dev = data.rolling(window=20).std()
    lower_band = moving_average - 2 * std_dev
    
    last_price = data.iloc[-1]
    last_rsi = rsi.iloc[-1]
    last_stochastic = stochastic.iloc[-1]
    last_lower_band = lower_band.iloc[-1]
    
    if last_price <= last_lower_band and last_rsi < 30 and last_stochastic < 20:
        return f"Com base nos indicadores, hoje é um bom dia para considerar a compra de {ticker}."
    else:
        return f"Com base nos indicadores, hoje não é um bom dia para comprar {ticker}."

ticker = "BBAS3"
data = fetch_stock_data(ticker)

plt.figure(figsize=(14, 10))

# Plotando preço e Bandas de Bollinger
plt.subplot(311)
data.plot(label='Preço', color='blue')
moving_average = data.rolling(window=20).mean()
std_dev = data.rolling(window=20).std()
upper_band = moving_average + 2 * std_dev
lower_band = moving_average - 2 * std_dev
moving_average.plot(label='Média Móvel de 20 Dias', color='black', linestyle='--')
upper_band.plot(label='Banda Superior de Bollinger', color='red', linestyle=':')
lower_band.plot(label='Banda Inferior de Bollinger', color='green', linestyle='--')
plt.title('Bandas de Bollinger para ' + ticker + ' (Últimos 60 Dias)')
plt.legend()

# Índice de Força Relativa (RSI)
plt.subplot(312)
rsi = calculate_rsi(data)
rsi.plot(label='RSI', color='purple')
plt.title('Índice de Força Relativa (Últimos 60 Dias)')
plt.axhline(70, color='red', linestyle='--')
plt.axhline(30, color='green', linestyle='--')
plt.legend()

# Oscilador Estocástico
plt.subplot(313)
stochastic = calculate_stochastic_oscillator(data)
stochastic.plot(label='Oscilador Estocástico', color='orange')
plt.title('Oscilador Estocástico (Últimos 60 Dias)')
plt.axhline(80, color='red', linestyle='--')
plt.axhline(20, color='green', linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()

buy_recommendation = check_buy_conditions(data, ticker)
print(buy_recommendation)