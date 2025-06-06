from fastapi import FastAPI, Request
from services.chat_service import generate_response

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the AI Regulation Chatbot!"}

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("question", "")
    answer = generate_response(query)
    return {"response": answer}