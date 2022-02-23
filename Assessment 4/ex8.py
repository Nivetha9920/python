import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/10'
data = {'id':10, 'userId':1, 'address+pincode':'chennai 600082', 'completed':'true'}
headers = {'Content-Type':'application/json; charset=UTF-8'}
response = requests.put(url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.ok)
print(response.content)
print(response.text)
print(type(response.text))
# https://jsonplaceholder.typicode.com/posts
print(response.url)
# application/json; charset=utf-8
print(response.headers['Content-Type'])
# utf-8
print(response.encoding)
