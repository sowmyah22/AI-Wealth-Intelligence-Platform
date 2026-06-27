def build_context(context="",history="",summary=""):
    combined_context=f"""
    Portfolio Summary:
{summary}

Portfolio Context:
{context}

Portfolio History:
{history}

    """
    return combined_context