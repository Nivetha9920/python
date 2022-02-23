import requests
data="https://jsonplaceholder.typicode.com/todos/10
response=requests.delete(data)
response.json()
response.status_code
