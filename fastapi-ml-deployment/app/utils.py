import os

API_TOKEN = os.getenv("API_TOKEN", "super-secret")

def is_authorized(headers):
    auth_header = headers.get("authorization")
    return auth_header == f"Bearer {API_TOKEN}"
