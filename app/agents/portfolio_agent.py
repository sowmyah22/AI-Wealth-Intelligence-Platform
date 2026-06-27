import ollama
from app.agents.tools import get_portfolio_history_tool, retrieve_portfolio_context_tool, get_portfolio_summary_tool
#from app.agents.agent_router import determine_tools
from app.agents.tool_selector import select_tools
from app.agents.context_builder import build_context

def portfolio_agent(user_query:str):
    #step 1:Retrieve history
    #history=get_portfolio_history_tool()
    #portfolio_summary=get_portfolio_summary_tool()

    #print("\n===== PORTFOLIO SUMMARY =====")
    #print(portfolio_summary)
    #print("\n==========")

    #step 2:Retrieve context
    #context=retrieve_portfolio_context_tool(user_query)
    #selected_tools=determine_tools(user_query)
    selected_tools=select_tools(user_query)

    #print(f"Selected tools: {selected_tools}")

    context= ""
    ## Creating and empty dict might cause keyerror so just assigning the keys before instead of wrong interpretations
    portfolio_summary={
    "portfolio_health": "Unknown",
    "diversification_score": "Unknown",
    "concentration_risk": "Unknown",
    "top_holding": "Unknown",
    "sector_exposure": {}
    }
   # question then the agent decides and selects the tools
    history=[]

    if "portfolio_context" in selected_tools:
        context=retrieve_portfolio_context_tool(user_query)
    if "portfolio_summary" in selected_tools:
        portfolio_summary=get_portfolio_summary_tool()
    if "portfolio_history" in selected_tools:
         history=get_portfolio_history_tool()
    
    print("\n===== AGENT THINKING =====")
    print("User Query:", user_query)
    print(f"selected tool:{selected_tools}")
    print("=========================\n")

    combined_context=build_context(
        context=context,
        history=history,
        summary=portfolio_summary
    )
    print("\n===== AGENT OBSERVATION =====")
    print(combined_context)
    print("=============================\n")    
    #step 3 :prompt
#     Portfolio Context:
# {context}

# Portfolio Health:
# {portfolio_summary["portfolio_health"]}

# Diversification Score:
# {portfolio_summary["diversification_score"]}

# Concentration Risk:
# {portfolio_summary["concentration_risk"]}

# Top Holding:
# {portfolio_summary["top_holding"]}

# Sector Exposure:
# {portfolio_summary["sector_exposure"]}

# Portfolio History:
# {history}
    prompt = f"""
You are an autonomous AI Financial Portfolio Agent.

IMPORTANT:

The portfolio summary values come from the analytics engine.

Use them exactly as provided.

Do not reinterpret:
- Portfolio Health
- Diversification Score
- Concentration Risk
- Top Holding Allocation

Repeat these values exactly when discussing the portfolio.
not percentages.Do not convert them into percentages.

User Question:
{user_query}

Relevant Portfolio Information:{combined_context}

Your responsibilities:
- analyze portfolio risks
- detect diversification issues
- provide actionable insights
- use ONLY the portfolio information provided
- do not invent financial metrics
- do not calculate VaR or Sharpe ratio unless explicitly provided

Generate a concise professional financial analysis.
"""

    #step 4:LLM Reasoning and Analysis
    response=ollama.chat(model="llama3",messages=[{"role":"user", "content":prompt}])
    return response["message"]["content"]