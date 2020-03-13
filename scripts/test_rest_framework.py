import requests
import json
import os

ENDPOINT = 'http://127.0.0.1:8000/auth/'
POST_ENDPOINT = 'http://127.0.0.1:8000/api/status/'

user = {
    'username': 'rezsj78',
    'password': 'sherlock761'
}

headers = {
    'content-type': 'application/json'
}

res = requests.post(ENDPOINT, data=json.dumps(user), headers=headers)
print(res.status_code)
print(res.text)
