import yfinance as yf

def get_stock_market_data(stock:str):
    ticker=yf.Ticker(stock)
    info=ticker.info
    current_price = (
        info.get("currentPrice")
        or info.get("regularMarketPrice")
        or info.get("previousClose")
    )

    return {
        "current_price":current_price,
        "market_cap": info.get("marketCap"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "pe_ratio": info.get("trailingPE")
    }