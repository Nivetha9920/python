import requests
data="https://jsonplaceholder.typicode.com/todos/7
response=requests.delete(data)
response.json()
response.status_code
