# Api Endpoints for the application

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.services.ai_service import get_stock_analysis
from app.services.portfolio_service import analyze_portfolio
from app.models.portfolio import PortfolioRequest
from app.services.database_service import get_saved_portfolios
from app.rag.retrieval_service import retrieve_similar_context
from app.services.rag_ai_service import generate_rag_response
from app.agents.portfolio_agent import portfolio_agent


router=APIRouter()

# single stock analysis
#@router.get("/analyze")
#def analyze(stock:str):
 #   analysis=get_stock_analysis(stock)
    
  #  return {
    #     "stock":stock,
    #     "analysis":analysis
    # }

#portfolio intelligence
@router.post("/portfolio/analyze")
def portfolio_analysis(request:PortfolioRequest):
    result =analyze_portfolio(request.holdings)
    return result

#retrieve saved holdings
@router.get("/portfolio/history")
def portfolio_history():
    holdings=get_saved_portfolios()
    result=[]

    for holding in holdings:
        result.append(
            {
                "id":holding.id,
                "stock":holding.stock,
                "quantity":holding.quantity,
                "buy_price":holding.buy_price
            }
        )
    return {
        "history":result
    }

@router.get("/portfolio/retrieve")
def retrieve_context(query:str):
    results=retrieve_similar_context(query)
    return {
        "query":query,
        "result":results
    }

@router.get("/portfolio/ask", response_class=PlainTextResponse)
def ask_portfolio_ai(query: str):
    return generate_rag_response(query)

@router.get("/portfolio/agent", response_class=PlainTextResponse)
def ask_portfolio_agent(query: str):
    return portfolio_agent(query)