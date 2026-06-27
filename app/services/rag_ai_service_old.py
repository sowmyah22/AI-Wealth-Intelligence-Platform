## Create Rag AI Serivce 

from app.rag.retrieval_service import retrieve_similar_context


def generate_rag_response(user_query:str):
    contexts=retrieve_similar_context(user_query)
    combined_context="\n".join(contexts) # Context Injection
    # Template Response (multiline string — real line breaks, not escaped \\n)
    response = f"""Finance AI Analysis

User Question:
{user_query}

Relevant Portfolio Context:
{combined_context}

AI Insights:
Based on your portfolio context, there appears to be concentration exposure that should be monitored.
"""
    return response