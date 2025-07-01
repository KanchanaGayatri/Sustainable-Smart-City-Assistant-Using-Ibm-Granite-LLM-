from fastapi import FastAPI
from pydantic import BaseModel
from app.services.sustainability_report import generate_sustainability_report
from app.services.chat_assistant import chat_with_user

# ✅ Import your service functions
from app.services.kpi_forecast import forecast_kpi
from app.services.anomaly_detection import detect_anomalies
from app.services.eco_tips import generate_eco_tips

app = FastAPI()

# ✅ Root path to verify API is running
@app.get("/")
def read_root():
    return {"message": "Smart City Assistant API is working."}

# ✅ Shared model
class PromptRequest(BaseModel):
    prompt: str

# ✅ Forecast route
@app.post("/forecast")
def forecast_kpi_endpoint(prompt: PromptRequest):
    result = forecast_kpi(prompt.prompt)
    return {"forecast": result}

# ✅ Anomalies route
@app.post("/anomalies")
def anomalies_endpoint(prompt: PromptRequest):
    dummy_data = [10, 15, 14, 13, 99, 12, 11]  # Replace with real logic if needed
    anomalies = detect_anomalies(dummy_data)
    return {"result": anomalies}

# ✅ Eco tips route
@app.post("/eco-tips")
def eco_tips_endpoint(prompt: PromptRequest):
    tips = generate_eco_tips(prompt.prompt)
    return {"tips": tips}
@app.post("/generate-report")
def generate_report_endpoint(prompt: PromptRequest):
    report = generate_sustainability_report(prompt.prompt)
    return {"report": report}
@app.post("/ask")
def chat_endpoint(prompt: PromptRequest):
    reply = chat_with_user(prompt.prompt)
    return {"response": reply}
