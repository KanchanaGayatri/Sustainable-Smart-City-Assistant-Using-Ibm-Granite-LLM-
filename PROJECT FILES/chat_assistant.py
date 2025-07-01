from app.services.granite_llm import ask_granite

def chat_with_user(prompt: str) -> str:
    instruction = (
        "You are a Smart City Assistant. Answer the user's question clearly:\n"
        f"User: {prompt}\n\n"
        "Assistant:"
    )
    return ask_granite(instruction)
