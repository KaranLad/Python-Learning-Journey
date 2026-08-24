import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# User ID input
user_id = input("Enter user ID: ")

# REST API URL
url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

# Send GET request
try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

    elif response.status_code == 404:
        print("User not found!")
        exit()

    elif response.status_code >= 500:
        print("Server error. Please try again later.")
        exit()

    else:
        print("API request failed.")
        exit()

except requests.exceptions.RequestException as e:
    print("Network error:", e)
    exit()


# Convert JSON response into Python data
data = response.json()

name = data["name"]
username = data["username"]
email = data["email"]
city = data["address"]["city"]

question = input("Ask Gemini: ")

print("API Data:", data)


# Create prompt for Gemini
clean_data = f"""
Name: {name}
Username: {username}
Email: {email}
City: {city}
"""
prompt = f"""
Here is the user data from an API:

{clean_data}

User question:
{question}

"""


# Send data to Gemini
gemini_response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)


# Print Gemini answer
print("\nGemini:", gemini_response.text)