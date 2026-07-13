from pydantic import BaseModel
from typing import List, Dict

class HoldingsSummary(BaseModel):
    stock:str
    allocation:float
    current_value:float
    profit_loss:float
    sector:str

class PortfolioIntelligence(BaseModel):
    portfolio_value: float
    portfolio_health: str
    diversification_score:int
    concentration_risk:str
    sector_distribution:Dict[str,float]
    top_holdings:List[HoldingsSummary]

class MarketStock(BaseModel):
    symbol:str
    price:float
    change:float
    change_percentage:float

class MarketIntelligence(BaseModel):
    market_status:str
    market_sentiment:str
    top_gainers:List[MarketStock]
    top_losers:List[str]
   
class Recommendations(BaseModel):
    stock:str
    category:str
    confidence:float
    reason:str
    supporting_factors:List[str]

class NewsItem(BaseModel):
    stock:str
    headline:str
    source:str
    sentiment:str
    
class MacroEvent(BaseModel):
    title:str
    impact:str
    
class DailyBrief(BaseModel):
    portfolio:PortfolioIntelligence
    market:MarketIntelligence
    news:List[NewsItem]
    recommendations:List[Recommendations]
    macro_events:List[MacroEvent]