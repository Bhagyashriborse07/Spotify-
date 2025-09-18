import requests
import base64

client_id = '413f0dd5ff874dbba8b667abc734ac31'
client_secret ='9cc64cfcca0e4fefb34104d2b718c9f9'

# Encode credentials
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Get token
url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {b64_auth_str}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}

response = requests.post(url, headers=headers, data=data)

# Print status and response for debugging
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
print("Access Token:", response.json().get("access_token"))
