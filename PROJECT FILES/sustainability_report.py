from app.services.granite_llm import ask_granite

def generate_sustainability_report(prompt: str) -> str:
    instruction = (
        "Generate a detailed sustainability report based on the following topic:\n"
        f"{prompt}\n\n"
        "The report should include key metrics, policies, and future suggestions."
    )
    return ask_granite(instruction)
