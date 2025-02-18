# need to pay for an API key


import requests

url = "https://api.heygen.com/v2/video/generate"

payload = {
    "caption": False,
    "dimension": {
        "width": 1280,
        "height": 720
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": "<your-api-key>"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)