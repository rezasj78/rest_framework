import requests

a = requests.get('http://127.0.0.1:8000/api/status/')
id = a.json()[0]['id']
print(id)
# b = requests.delete('http://127.0.0.1:8000/api/status/' + str(id) + '/')
# print(b.status_code)

# print(requests.codes)