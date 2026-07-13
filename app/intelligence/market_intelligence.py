from app.models.market import MarketIntelligence

def get_market_intelligence():
    return MarketIntelligence(
        market_status="Closed",
        market_sentiment="Neutral",
        top_gainers=[],
        top_losers=[]
    )