import requests

# URL API для получения курсов
exchanges = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=SOLUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=SOL-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=SOLUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=solusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=SOL_USDT"
}

# Функция для получения курсов с разных бирж
def get_price(exchange, url):
    response = requests.get(url)
    data = response.json()
    
    if exchange == "Binance":
        return float(data['askPrice']), float(data['bidPrice'])
    elif exchange == "KuCoin":
        return float(data['data']['bestAsk']), float(data['data']['bestBid'])
    elif exchange == "Bybit":
        return float(data['result'][0]['ask_price']), float(data['result'][0]['bid_price'])
    elif exchange == "Huobi":
        return float(data['tick']['ask'][0]), float(data['tick']['bid'][0])
    elif exchange == "Gate":
        tickers = data[0]  # Исправленная часть
        return float(tickers['last']), float(tickers['last'])  # Нужно уточнить структуру ответа API
    else:
        return None, None

# Основная функция для арбитража
while True:
    prices = {}
    for exchange, url in exchanges.items():
        ask, bid = get_price(exchange, url)
        prices[exchange] = {'ask': ask, 'bid': bid}

    # Поиск наилучшей цены для покупки и продажи
    best_bid = max(prices.items(), key=lambda x: x[1]['bid'])
    best_ask = min(prices.items(), key=lambda x: x[1]['ask'])

    if best_bid[1]['bid'] > best_ask[1]['ask']:
        print(f"Buy on {best_ask[0]} at {best_ask[1]['ask']} and sell on {best_bid[0]} at {best_bid[1]['bid']}")
    else:
        print("No arbitrage opportunity at the moment.")

    print("Prices:")
    for exchange, price in prices.items():
        print(f"{exchange} - Ask: {price['ask']}, Bid: {price['bid']}")
    
    print("\n")
