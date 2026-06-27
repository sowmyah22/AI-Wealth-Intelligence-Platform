# Portfolio score and portfolio health

from collections import Counter
import selectors
from app.data.stock_metadata import STOCK_METADATA


def caluclate_portfolio_score(stocks:list):
    stock_count=len(stocks)

    if stock_count>=5:
        diversification_score=9
        portfolio_health="Excelent"
    
    elif stock_count>=3:
        diversification_score=7
        portfolio_health="Good"

    else:
        diversification_score=4
        portfolio_health="Risky"

    return {
        "portfolio_health":portfolio_health,
        "diversification_score":diversification_score
    }

# Recommendations

def analyze_sector_exposure(stocks:list):

    sectors = []

    for stock in stocks:
        metadata=STOCK_METADATA.get(stock)

        if metadata:
            sectors.append(metadata["sector"])
    
    sector_count=Counter(sectors)

    return dict(sector_count)


def generate_recommendations(stocks:list):
    recommendations=[]

    sector_analysis=analyze_sector_exposure(stocks)

    for sector,count in sector_analysis.items():
        if count>=2:
            recommendations.append(
                f"High exposure detected in {sector} sector"
            )

        if len(sector_analysis)<=1:
            recommendations.append(
                "Portfolio lacks diversification"
            )
    return recommendations
        