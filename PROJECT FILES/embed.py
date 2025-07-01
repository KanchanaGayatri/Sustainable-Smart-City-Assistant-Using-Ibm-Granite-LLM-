# app/services/embed.py

import hashlib

def embed_text(text):
    # Simulated embedding using hash (replace with real embedding later)
    return [float(int(hashlib.sha256(text.encode()).hexdigest(), 16) % 1000) / 1000.0]
