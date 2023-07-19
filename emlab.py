"""Saurabh Deulkar """


import requests

api_endpoint = "https://api.pawan.krd/v1/chat/completions"
api_key = "pk-pSVHosorwvYrZzPVUnepgYvlLIkHRXjiCmOsHCzSDvWIeqNT"

while True:
    question = input("How can i help you, My master? (enter quit to end) :-")
    if question == "quit":
        break
    params = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 300,
        "messages": [
            {"role": "user", "content":question}
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(api_endpoint, json=params, headers=headers)
    data = response.json()

    print(data["choices"][0]['message']['content'])