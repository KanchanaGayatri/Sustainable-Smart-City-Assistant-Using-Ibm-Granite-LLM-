from dotenv import load_dotenv
import os

load_dotenv()

print("Current folder:", os.getcwd())
print("IBM_API_KEY:", os.getenv("IBM_API_KEY"))
print("PROJECT_ID:", os.getenv("PROJECT_ID"))
print("MODEL_ID:", os.getenv("MODEL_ID"))
