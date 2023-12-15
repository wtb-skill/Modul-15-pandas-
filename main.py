import pandas as pd
import matplotlib.pyplot as plt

# Dane
prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25),

]

# Tworzenie DataFrame
df = pd.DataFrame(prices, columns=['Month', 'PricePLN'])

# Ustawienie miesiąca jako indeksu
df.set_index('Month', inplace=True)

# Dodanie kolumny z ceną w dolarach
df['PriceUSD'] = df['PricePLN'] / 4.0  # Przelicznik 1 USD = 4 PLN

# Wyświetlenie wykresu
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['PriceUSD'], 'r--')
plt.xlabel('Month')
plt.ylabel('Price in USD')
plt.title('Price of goods (USD)')
plt.xticks(df.index)  # Setting x-axis ticks to correspond to months
plt.grid(True)
plt.show()
