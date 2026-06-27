# Create Vector store
import chromadb

client=chromadb.PersistentClient(path="./chroma_db") # embeddings are stored permanently
collection=client.get_or_create_collection(name="porfolio_memory")

def store_portfolio_memory(doc_id:str,text:str,embedding):
    collection.add(
        ids=[doc_id], #unique id
        documents=[text], # original text
        embeddings=[embedding]) #vector embedding