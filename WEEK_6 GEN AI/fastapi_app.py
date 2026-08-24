# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     city: str

# @app.get("/")

# def home():
#     return{"message": "Hello, FastAPI!"}

# @app.get("/user")
# def user():
#     return {
#         "name": "Karan Lad",
#         "age": 22,
#         "city": "Bilimora" 
#     }
# @app.post("/user")
# def create_user(user: User):
#     return {
#         "message": "User created successfully",
#         "user": user
#     }

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class ChatRequest(BaseModel):
#     message: str


# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI"}


# @app.post("/chat")
# def chat(request: ChatRequest):
#     return {
#         "message": request.message
#     }


# FastAPI + Gemini API
# This API takes a user's message and sends it to Gemini AI
# Then it returns the AI-generated response

import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

app = FastAPI()

def load_history():
    with open("history.json","r") as file:
        return json.load(file)

def save_history(history):
    with open("history.json","w") as file:
        json.dump(history,file,indent=4)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.post("/chat")
def chat(request: ChatRequest):

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=request.message
        )

        # Load old chat history
        history = load_history()

        # Add new user message and AI response
        history.append({
            "user": request.message,
            "ai": response.text
        })

        save_history(history)

        return{
            "response": response.text
        }

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again later."
            )

        elif "404" in error_message:
            raise HTTPException(
                status_code=404,
                detail="Gemini model was not found or is unavailable."
            )

        elif "503" in error_message:
            raise HTTPException(
                status_code=503,
                detail="Gemini service is temporarily unavailable. Please try again."
            )

        else:
            raise HTTPException(
                status_code=500,
                detail="Something went wrong with the AI service."
            )
@app.get("/history")
def get_history():

    history = load_history()

    return {
        "history": history
    }


@app.delete("/history")
def clear_history():

    save_history([])

    return {
        "message": "Chat history cleared successfully"
    }