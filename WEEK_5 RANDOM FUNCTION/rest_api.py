import requests


# ================= GET REQUEST =================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.status_code)

data = response.json()

print(data[0]["name"])


# ================= GET WITH QUERY PARAMETERS =================

params = {
    "id": 5
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params=params
)

data = response.json()

print(data[0]["name"])


# ================= POST REQUEST =================

data = {
    "name": "Karan",
    "skill": "Python",
    "age": 22
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print(response.status_code)
print(response.json())


# ================= HEADERS =================

headers = {
    "Content-Type": "application/json"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(response.status_code)


# ================= API KEY =================
# API key is a secret value used to identify
# and authorize access to an API.

headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(response.status_code)


# ================= PUT REQUEST =================
# PUT → completely update/replace existing data

data = {
    "name": "Karan",
    "skill": "Python"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.status_code)
print(response.json())


# ================= PATCH REQUEST =================
# PATCH → update specific part of existing data

data = {
    "skill": "Gen AI"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/users/1",
    json=data
)

print(response.status_code)
print(response.json())


# ================= DELETE REQUEST =================

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)


# ================= ERROR HANDLING =================

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("API Error:", e)

# ================= (.env) Environment Variables =================
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)