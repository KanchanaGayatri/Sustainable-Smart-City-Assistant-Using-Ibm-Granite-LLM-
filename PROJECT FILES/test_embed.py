from app.services.document_embedder import embed_document

with open("policy.txt", "r") as file:
    content = file.read()

print(embed_document("doc1", content))
