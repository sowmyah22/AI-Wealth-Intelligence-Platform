
## It helps in choosing the tools instead of all the tools Rule-based
def determine_tools(user_query:str):
    query=user_query.lower()
    tools=[]

    if 'risk' in query:
        tools.append("portfolio_summary")
    if 'diversify' in query:
        tools.append("portfolio_summary")
    if 'holding' in query:
        tools.append("portfolio_history")
    if 'improve' in query:
        tools.append("portfolio_context")
        tools.append("portfolio_summary")
    return tools

    