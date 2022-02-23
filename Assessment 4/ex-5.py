res = requests.get('https://jsonplaceholder.typicode.com/todos')
json = res.json()
print(json[0:5])
