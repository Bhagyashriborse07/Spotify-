import requests

access_token = "BQBdKlTpO1IgtJ5ZSY5u0W_xzKaTSR4VeSeAqOP5XnWqyKB8lYIDtBY2NzRpQuVq_MgWdIvQyBIP28mKZWtWMkSpz5XQa3gdieWFBy_udGx9m1feQQ23vzI_tpCHapVCCTLCmsXR5Os"  # Paste the token you got here

artist_id = "1vCWHaC5f2uS3yhpwWbIA6"  # Example: Avicii

url = f"https://api.spotify.com/v1/artists/{artist_id}"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
