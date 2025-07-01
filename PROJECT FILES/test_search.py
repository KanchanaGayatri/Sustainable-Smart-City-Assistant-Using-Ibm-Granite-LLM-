# test_search.py

from app.services.semantic_search import semantic_search

query = "How can smart cities reduce traffic?"
results = semantic_search(query)

print("Search Results:")
for i, result in enumerate(results, 1):
    print(f"{i}. {result}")
