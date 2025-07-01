# create_index.py

import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load API key from .env
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

# Initialize client
pc = Pinecone(api_key=api_key)

# Replace with your correct index name
index_name = "smart-city-index"

# Create the index if it doesn’t exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # or the dimension used by your embed_text
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"  # ✅ Use the correct region if different
        )
    )
    print(f"✅ Index '{index_name}' created.")
else:
    print(f"ℹ️ Index '{index_name}' already exists.")
