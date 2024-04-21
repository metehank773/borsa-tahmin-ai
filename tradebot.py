import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf
import datetime

def get_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print("Hata:", e)
        return None

# Kullanıcıdan hisse sembolünü alınması
symbol = input("Lütfen hisse sembolünü girin (örn. GARAN.IS): ")

# Veri aralığını belirleme
start_date = datetime.datetime(2024, 4, 1)
end_date = datetime.datetime(2024,4,21)

# Hisse fiyatlarını al
data = get_stock_data(symbol, start_date, end_date)

if data is not None:
    # Verileri görselleştirme
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Hisse Fiyatları', color='b')
    plt.title(f'{symbol} Hisse Fiyatları')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.xticks(rotation=45)  # Tarihleri 45 derece döndür
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

    # Özellikleri ayarlama
    if isinstance(data.index, pd.DatetimeIndex):  # Veri tipini kontrol et
        data['Day'] = data.index.day
        data['Month'] = data.index.month
        data['Year'] = data.index.year
        data['Weekday'] = data.index.weekday
    else:
        data.reset_index(inplace=True)
        data['Date'] = pd.to_datetime(data['Date'])
        data['Day'] = data['Date'].dt.day
        data['Month'] = data['Date'].dt.month
        data['Year'] = data['Date'].dt.year
        data['Weekday'] = data['Date'].dt.weekday
        data.set_index('Date', inplace=True)

    # Bağımsız ve bağımlı değişkenleri belirleme
    X = data[['Day', 'Month', 'Year', 'Weekday']]
    y = data['Close']

    # Lineer regresyon modeli oluşturma ve eğitme
    model = LinearRegression()
    model.fit(X, y)

    # Tahminleri yapma
    future_dates = pd.date_range(start=data.index[-1], periods=31) # Son tarihten itibaren 31 günlük bir süre
    future_data = pd.DataFrame({'Day': future_dates.day, 'Month': future_dates.month,
                                'Year': future_dates.year, 'Weekday': future_dates.weekday}, index=future_dates)
    predicted_prices = model.predict(future_data)

    # Tahmin edilen fiyatları görselleştirme
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Gerçek Fiyatlar', color='b')
    plt.plot(future_dates, predicted_prices, label='Tahmin Edilen Fiyatlar', color='r', linestyle='--')
    plt.title(f'{symbol} Hisse Fiyatları: Tahmin Edilen ve Gerçek')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.xticks(rotation=20)  # Tarihleri 45 derece döndür
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

    # Modelin performansını değerlendirme
    print("Model Performansı:")
    print("Ortalama Kare Hatası (MSE):", mean_squared_error(y, model.predict(X)))
    print("R-kare değeri (R^2):", r2_score(y, model.predict(X)))