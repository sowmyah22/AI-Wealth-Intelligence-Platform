from app.services.ai_service import get_stock_analysis
from app.services.market_service import get_stock_market_data
from app.data.stock_metadata import STOCK_METADATA
from app.services.scoring_service import caluclate_portfolio_score,generate_recommendations,analyze_sector_exposure
from app.services.valuation_service import calculate_holding_value,calculate_invested_value,calculate_profit_loss
from app.services.allocation_service import calculate_allocation_percentage,find_top_holding
from app.services.database_service import save_portfolio_holdings
from app.rag.embedding_service import generate_embedding
from app.rag.chroma_service import store_portfolio_memory


def analyze_portfolio(holdings:list):

    #Save to database
    save_portfolio_holdings(holdings)
    portfolio_analysis=[]
    total_portfolio_value=0

    for holding in holdings:  # Build Holdings data
        stock=holding.stock
        quantity=holding.quantity
        buy_price=holding.buy_price
        analysis=get_stock_analysis(stock)
        metadata=STOCK_METADATA.get(stock)
        market_data={}  
        current_price=0   # to avoid UnboundLocalError

        if metadata:
            ticker=metadata["ticker"]

            market_data=get_stock_market_data(ticker)

            current_price=(market_data.get("current_price") or 0) # 0 to avoid return none

            invested_value=calculate_invested_value(quantity,buy_price)

            current_value=calculate_holding_value(quantity,current_price)

            profit_loss=calculate_profit_loss(invested_value,current_value)

            total_portfolio_value += current_value


            portfolio_analysis.append({
            "stock":stock,
            "quantity":quantity,
            "buy_price":buy_price,
            "current_price":current_price,
            "invested_price":invested_value,
            "current_value":current_value,
            "profit_loss":profit_loss,
            "analysis":analysis,
            "market_data":market_data
             })

    for item in portfolio_analysis: #allocation calculation
        allocation_percentage=calculate_allocation_percentage(
        item["current_value"],
        total_portfolio_value
        )
        item["allocation_percentage"]=allocation_percentage

    top_holding=find_top_holding(portfolio_analysis) #Top holdings
    concentration_risk="Low"

    if top_holding:
        if top_holding["allocation_percentage"]>50:
            concentration_risk="High"

        elif top_holding["allocation_percentage"]>30:
            concentration_risk="Moderate"

    portfolio_commentary=[] #commentary
    if top_holding:
        portfolio_commentary.append(
            f"{top_holding['stock']} is your largest holding "
            f"at {top_holding['allocation_percentage']}% allocation."
        )
    if concentration_risk == "High":
        portfolio_commentary.append(
        "Portfolio shows high concentration risk."
        )

    elif concentration_risk == "Moderate":
        portfolio_commentary.append(
        "Portfolio has moderate concentration risk."
        )
    
    else:
         portfolio_commentary.append(
        "Portfolio appears reasonably diversified."
        )
    
    for idx,comment in enumerate(portfolio_commentary): #It allows you to track the index and the item simultaneously during a loop 
        embedding=generate_embedding(comment)
        store_portfolio_memory(doc_id=f"comment_{idx}",text=comment,embedding=embedding)
   # Portfolio scoring

    score_data=caluclate_portfolio_score(
        [holding.stock for holding in holdings]
    )

    recommendations=generate_recommendations(
        [holding.stock for holding in holdings]
    )

    sector_analysis=analyze_sector_exposure(
        [holding.stock for holding in holdings]
        )

    return {
        "total_portfolio_value":total_portfolio_value,
        "portfolio_health":score_data["portfolio_health"],
        "diversification_score":score_data["diversification_score"],
        "sector_exposure":sector_analysis,
        "concentration_risk":concentration_risk,
        "top_holding":top_holding,
        "recommendations":recommendations,
        "portfolio_commentary":portfolio_commentary,
        "holdings":portfolio_analysis
    }