import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 11,"title": "Macaroni", "completed": False}
response = requests.post(api_url, json=todo)
response.json()
response.status_code
