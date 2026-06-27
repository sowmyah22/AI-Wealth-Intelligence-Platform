import ollama

Available_tools=[
    "portfolio_summary",
    "portfolio_history",
    "portfolio_context"
]

def select_tools(user_query:str):
    prompt=f"""
    You are an AI tool selector.

Available Tools:

1. portfolio_summary
   - portfolio health
   - diversification score
   - concentration risk
   - top holding

2. portfolio_context
   - retrieved portfolio memory
   - previous portfolio insights

3. portfolio_history
   - stock holdings
   - quantity
   - buy price

User Question: {user_query}

Return only a comma seperated list of required tools

Example:

portfolio_summary

or

portfolio_summary,portfolio_context

"""

    response=ollama.chat(
        model="llama3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    result=response["message"]["content"]
    print("\n===Raw Tools=====")
    print(result)
    selected_tools=[]
    for tool in Available_tools:
         if tool in result:
            selected_tools.append(tool)

    print("selected_tools",selected_tools)

    return selected_tools