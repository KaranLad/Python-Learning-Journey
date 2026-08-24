import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key loaded:", bool(api_key))

client = genai.Client(api_key=api_key)


# ========== Save History ==========
def save_history():
    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)


# ========== Load History ==========
def load_history():
    with open("history.json", "r") as file:
        return json.load(file)


# ========== Load Previous History ==========
if os.path.exists("history.json"):
    history = load_history()
    print("Previous chat loaded")
else:
    history = []


# ========== Chat Loop ==========
while True:

    question = input("You: ")

    # Empty input
    if not question.strip():
        continue

    # Exit
    if question.lower() == "exit":
        print("Chat ended.")
        break

    # Clear
    if question.lower() == "clear":
        history.clear()
        save_history()
        print("Chat cleared!")
        continue

    # History
    if question.lower() == "history":
        for message in history:
            print(message)
        continue

    try:

        # Create context from previous history
        context = "\n".join(history)

        prompt = context + "\nYou: " + question

        # Streaming response
        response = client.models.generate_content_stream(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        print("Gemini:", end=" ")

        full_response = ""

        for chunk in response:
            print(chunk.text, end="")
            full_response += chunk.text

        print()

        # Save conversation
        history.append("You: " + question)
        history.append("Gemini: " + full_response)

        save_history()

    except Exception as e:

        error = str(e)

        if "429" in error:
            print("Error: API quota exceeded. Please try again later.")

        elif "503" in error:
            print("Error: Gemini service is temporarily unavailable.")

        elif "400" in error:
            print("Error: Invalid request.")

        else:
            print("Error:", e)