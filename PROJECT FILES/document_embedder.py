import os
import pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# Initialize Pinecone
import os
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = os.getenv("INDEX_NAME")

# Check if index exists, else create
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Match MiniLM embedding size
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region=os.getenv("PINECONE_ENV")
        )
    )

index = pc.Index(index_name)


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_document(doc_id, text):
    # Split text into chunks of 300 characters
    chunks = [text[i:i+300] for i in range(0, len(text), 300)]
    embeddings = model.encode(chunks).tolist()

    # Prepare and upload vectors to Pinecone
    to_upsert = [
        (f"{doc_id}_{i}", vector, {"text": chunk})
        for i, (chunk, vector) in enumerate(zip(chunks, embeddings))
    ]
    index.upsert(vectors=to_upsert)
    return f"✅ Uploaded {len(to_upsert)} chunks to Pinecone for document '{doc_id}'"
