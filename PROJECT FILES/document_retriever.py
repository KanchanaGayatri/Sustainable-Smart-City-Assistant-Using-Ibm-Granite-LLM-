from app.services.document_embedder import model, index

def search_policy(query, top_k=3):
    # Convert query to vector
    query_vector = model.encode([query])[0].tolist()

    # Perform semantic search
    results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)

    # Extract matching chunks
    return [match["metadata"]["text"] for match in results["matches"]]
