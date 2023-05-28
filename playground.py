import requests
import json

url = "https://graph.facebook.com/LATEST-API-VERSION/PAGE-ID/messages"

payload = {
    "recipient": {"id": "IGSID"},
    "message": {"text": "testing"}
}

params = {
    "access_token": "EAADNlHkTXi4BAHD74u1b0mBPzSqXIkswtMW7QsnzRlHLLbKfzKRZAQZBFgA22t5UaaJSrURHcVNFbKAjoGJX2jLbHfL5CZASU0bRQcgDzDe3DrY0geZBkZCCEBbbwsK5vnAhEeJuvG9l1Nrf1VKPHVigmYAXcaBpW7C1kBAhKXEa3xAqfO6zz8Dhh7Inj8dMZD"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, params=params, headers=headers, data=json.dumps(payload))

print(response.text)