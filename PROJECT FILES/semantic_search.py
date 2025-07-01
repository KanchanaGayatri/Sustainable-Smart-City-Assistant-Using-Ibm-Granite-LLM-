# app/services/semantic_search.py

import os
from dotenv import load_dotenv
from pinecone import Pinecone
from app.services.embed import embed_text  # This function must return a list of floats

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get API key and index name from environment
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME", "smart-city-index")

# ✅ Initialize Pinecone client
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)

def semantic_search(query):
    # Step 1: Embed the query
    query_embedding = embed_text(query)  # List of floats

    # Step 2: Query Pinecone
    search_response = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    # Step 3: Collect results
    results = []
    for match in search_response.get("matches", []):
        text = match.get("metadata", {}).get("text", "[No text found]")
        results.append(text)

    return results
