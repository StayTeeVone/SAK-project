import requests

# URL API для получения курсов
exchanges_SOL = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=SOLUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=SOL-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=SOLUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=solusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=SOL_USDT"
}

exchanges_BTC = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=BTCUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=btcusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT"
}

exchanges_ETH = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=ETHUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=ETH-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=ETHUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=ethusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=ETH_USDT"
}

exchanges_LINK = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=LINKUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=LINK-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=LINKUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=linkusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=LINK_USDT"
}

exchanges_DOGE = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=DOGEUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DOGE-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=DOGEUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=dogeusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=DOGE_USDT"
}

exchanges_CAKE = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=CAKEUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=CAKE-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=CAKEUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=cakeusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=CAKE_USDT"
}

exchanges_HOOK = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=HOOKUSDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=HOOKUSDT",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=HOOK_USDT"
}

exchanges_DASH = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=DASHUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DASH-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=DASHUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=dashusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=DASH_USDT"
}

exchanges_DODO = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=DODOUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DODO-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=DODOUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=dodousdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=DODO_USDT"
}

exchanges_EGLD = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=EGLDUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=EGLD-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=EGLDUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=egldusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=EGLD_USDT"
}

exchanges_LTC = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=LTCUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=LTC-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=LTCUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=ltcusdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=LTC_USDT"
}

exchanges_NEO = {
    "Binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=NEOUSDT",
    "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=NEO-USDT",
    "Bybit": "https://api.bybit.com/v2/public/tickers?symbol=NEOUSDT",
    "Huobi": "https://api.huobi.pro/market/detail/merged?symbol=neousdt",
    "Gate": "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=NEO_USDT"
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
    prices_SOL = {}
    for exchange, url in exchanges_SOL.items():
        ask, bid = get_price(exchange, url)
        prices_SOL[exchange] = {'ask': ask, 'bid': bid}

    prices_BTC = {}
    for exchange, url in exchanges_BTC.items():
        ask, bid = get_price(exchange, url)
        prices_BTC[exchange] = {'ask': ask, 'bid': bid}

    prices_ETH = {}
    for exchange, url in exchanges_ETH.items():
        ask, bid = get_price(exchange, url)
        prices_ETH[exchange] = {'ask': ask, 'bid': bid}

    prices_LINK = {}
    for exchange, url in exchanges_LINK.items():
        ask, bid = get_price(exchange, url)
        prices_LINK[exchange] = {'ask': ask, 'bid': bid}

    prices_DOGE = {}
    for exchange, url in exchanges_DOGE.items():
        ask, bid = get_price(exchange, url)
        prices_DOGE[exchange] = {'ask': ask, 'bid': bid}

    prices_CAKE = {}
    for exchange, url in exchanges_CAKE.items():
        ask, bid = get_price(exchange, url)
        prices_CAKE[exchange] = {'ask': ask, 'bid': bid}

    prices_HOOK = {}
    for exchange, url in exchanges_HOOK.items():
        ask, bid = get_price(exchange, url)
        prices_HOOK[exchange] = {'ask': ask, 'bid': bid}

    prices_DASH = {}
    for exchange, url in exchanges_DASH.items():
        ask, bid = get_price(exchange, url)
        prices_DASH[exchange] = {'ask': ask, 'bid': bid}

    prices_DODO = {}
    for exchange, url in exchanges_DODO.items():
        ask, bid = get_price(exchange, url)
        prices_DODO[exchange] = {'ask': ask, 'bid': bid}

    prices_EGLD = {}
    for exchange, url in exchanges_EGLD.items():
        ask, bid = get_price(exchange, url)
        prices_EGLD[exchange] = {'ask': ask, 'bid': bid}

    prices_LTC = {}
    for exchange, url in exchanges_LTC.items():
        ask, bid = get_price(exchange, url)
        prices_LTC[exchange] = {'ask': ask, 'bid': bid}

    prices_NEO = {}
    for exchange, url in exchanges_NEO.items():
        ask, bid = get_price(exchange, url)
        prices_NEO[exchange] = {'ask': ask, 'bid': bid}    

    # Поиск наилучшей цены для покупки и продажи
    best_bid_SOL = max(prices_SOL.items(), key=lambda x: x[1]['bid'])
    best_ask_SOL = min(prices_SOL.items(), key=lambda x: x[1]['ask'])

    best_bid_BTC = max(prices_BTC.items(), key=lambda x: x[1]['bid'])
    best_ask_BTC = min(prices_BTC.items(), key=lambda x: x[1]['ask'])

    best_bid_ETH = max(prices_ETH.items(), key=lambda x: x[1]['bid'])
    best_ask_ETH = min(prices_ETH.items(), key=lambda x: x[1]['ask'])

    best_bid_LINK = max(prices_LINK.items(), key=lambda x: x[1]['bid'])
    best_ask_LINK = min(prices_LINK.items(), key=lambda x: x[1]['ask'])

    best_bid_DOGE = max(prices_DOGE.items(), key=lambda x: x[1]['bid'])
    best_ask_DOGE = min(prices_DOGE.items(), key=lambda x: x[1]['ask'])

    best_bid_CAKE = max(prices_CAKE.items(), key=lambda x: x[1]['bid'])
    best_ask_CAKE = min(prices_CAKE.items(), key=lambda x: x[1]['ask'])

    best_bid_HOOK = max(prices_HOOK.items(), key=lambda x: x[1]['bid'])
    best_ask_HOOK = min(prices_HOOK.items(), key=lambda x: x[1]['ask'])

    best_bid_DASH = max(prices_DASH.items(), key=lambda x: x[1]['bid'])
    best_ask_DASH = min(prices_DASH.items(), key=lambda x: x[1]['ask'])

    best_bid_DODO = max(prices_DODO.items(), key=lambda x: x[1]['bid'])
    best_ask_DODO = min(prices_DODO.items(), key=lambda x: x[1]['ask'])

    best_bid_EGLD = max(prices_EGLD.items(), key=lambda x: x[1]['bid'])
    best_ask_EGLD = min(prices_EGLD.items(), key=lambda x: x[1]['ask'])

    best_bid_LTC = max(prices_LTC.items(), key=lambda x: x[1]['bid'])
    best_ask_LTC = min(prices_LTC.items(), key=lambda x: x[1]['ask'])

    best_bid_NEO = max(prices_NEO.items(), key=lambda x: x[1]['bid'])
    best_ask_NEO = min(prices_NEO.items(), key=lambda x: x[1]['ask'])

    if best_bid_SOL[1]['bid'] > best_ask_SOL[1]['ask']:
        print('🛑SOLANA🛑')
        print(f"Buy SOL on {best_ask_SOL[0]} at {best_ask_SOL[1]['ask']} and sell on {best_bid_SOL[0]} at {best_bid_SOL[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_BTC[1]['bid'] > best_ask_BTC[1]['ask']:
        print('🛑BITCOIN🛑')
        print(f"Buy BTC on {best_ask_BTC[0]} at {best_ask_BTC[1]['ask']} and sell on {best_bid_BTC[0]} at {best_bid_BTC[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_ETH[1]['bid'] > best_ask_ETH[1]['ask']:
        print('🛑ETHEREUM🛑')
        print(f"Buy ETH on {best_ask_ETH[0]} at {best_ask_ETH[1]['ask']} and sell on {best_bid_ETH[0]} at {best_bid_ETH[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_LINK[1]['bid'] > best_ask_LINK[1]['ask']:
        print('🛑LINK🛑')
        print(f"Buy LINK on {best_ask_LINK[0]} at {best_ask_LINK[1]['ask']} and sell on {best_bid_LINK[0]} at {best_bid_LINK[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_DOGE[1]['bid'] > best_ask_DOGE[1]['ask']:
        print('🛑DOGE🛑')
        print(f"Buy DOGE on {best_ask_DOGE[0]} at {best_ask_DOGE[1]['ask']} and sell on {best_bid_DOGE[0]} at {best_bid_DOGE[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_CAKE[1]['bid'] > best_ask_CAKE[1]['ask']:
        print('🛑CAKE🛑')
        print(f"Buy CAKE on {best_ask_CAKE[0]} at {best_ask_CAKE[1]['ask']} and sell on {best_bid_CAKE[0]} at {best_bid_CAKE[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_HOOK[1]['bid'] > best_ask_HOOK[1]['ask']:
        print('🛑HOOK🛑')
        print(f"Buy HOOK on {best_ask_HOOK[0]} at {best_ask_HOOK[1]['ask']} and sell on {best_bid_HOOK[0]} at {best_bid_HOOK[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_DASH[1]['bid'] > best_ask_DASH[1]['ask']:
        print('🛑DASH🛑')
        print(f"Buy DASH on {best_ask_DASH[0]} at {best_ask_DASH[1]['ask']} and sell on {best_bid_DASH[0]} at {best_bid_DASH[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_DODO[1]['bid'] > best_ask_DODO[1]['ask']:
        print('🛑DODO🛑')
        print(f"Buy DODO on {best_ask_DODO[0]} at {best_ask_DODO[1]['ask']} and sell on {best_bid_DODO[0]} at {best_bid_DODO[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_EGLD[1]['bid'] > best_ask_EGLD[1]['ask']:
        print('🛑EGLD🛑')
        print(f"Buy EGLD on {best_ask_EGLD[0]} at {best_ask_EGLD[1]['ask']} and sell on {best_bid_EGLD[0]} at {best_bid_EGLD[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_LTC[1]['bid'] > best_ask_LTC[1]['ask']:
        print('🛑LTC🛑')
        print(f"Buy LTC on {best_ask_LTC[0]} at {best_ask_LTC[1]['ask']} and sell on {best_bid_LTC[0]} at {best_bid_LTC[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")

    if best_bid_NEO[1]['bid'] > best_ask_NEO[1]['ask']:
        print('🛑NEO🛑')
        print(f"Buy NEO on {best_ask_NEO[0]} at {best_ask_NEO[1]['ask']} and sell on {best_bid_NEO[0]} at {best_bid_NEO[1]['bid']}\n")
    else:
        print("No arbitrage opportunity at the moment.\n")    

    print('\n')

    # print("Prices:")
    # for exchange, price in prices.items():
    #     print(f"{exchange} - Ask: {price['ask']}, Bid: {price['bid']}")
