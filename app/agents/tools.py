from app.services.database_service import get_saved_portfolios
from app.rag.retrieval_service import retrieve_similar_context
from app.services.portfolio_service import analyze_portfolio

def get_portfolio_history_tool():
    history=get_saved_portfolios()
    results=[]
    for holding in history:
        results.append({
            "stock":holding.stock,
            "quantity":holding.quantity,
            "buy_price":holding.buy_price
        })
    return results

def retrieve_portfolio_context_tool(query:str):
    return retrieve_similar_context(query)

# This tool runs the existing analyze_portfolio function to get a summary of the portfolio.
def get_portfolio_summary_tool():
    history=get_saved_portfolios()
    holdings=[]
    for item in history:
        class Holding:
            pass
        h=Holding()

        h.stock=item.stock
        h.quantity=item.quantity
        h.buy_price=item.buy_price
        holdings.append(h)
    return analyze_portfolio(holdings)
