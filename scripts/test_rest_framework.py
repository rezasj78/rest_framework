import requests
import json
import os

ENDPOINT = 'http://127.0.0.1:8000/auth/'
POST_ENDPOINT = 'http://127.0.0.1:8000/api/status/'
CREATE_ENDPOINT = ENDPOINT + 'register/'

user = {
    "username": "rezasj78",
    "password": "sherlock761"
}

headers_1 = {
    'Content-type': 'application/json',
}

file = open('token.json', 'rb')
token = json.load(file)['token']
print(token)

headers_2 = {
    "Content-type": "application/json",
    # 'Authorization': 'JWT ' + token
}


json_data = {
    'user': 'reza2',
    'password': 'sherlock761',
    'password2': 'sherlock761',
    'email': 'sahraeianreza3rd@gmail.com'
}
res2 = requests.post(CREATE_ENDPOINT, data=json.dumps(json_data), headers=headers_2)
print(res2.text)
