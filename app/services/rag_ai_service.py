import ollama
from app.rag.retrieval_service import retrieve_similar_context

def generate_rag_response(user_query:str):
    contexts=retrieve_similar_context(user_query)
    combined_context="\n".join(contexts)
    prompt=f"""You are an AI Financial Analyst

    Analyze the user's portfolio usin the retrieved portfolio context.

User Question:
{user_query}

Portfolio Context:
{combined_context}

Provide:
Provide a concise financial analysis
in under 120 words.
Focus only on the most important
portfolio risks and suggestions.

"""
    response=ollama.chat(
        model="phi3",#"llama3",#"phi3"
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response["message"]["content"]