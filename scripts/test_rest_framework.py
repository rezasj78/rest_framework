import requests
import json
import os

ENDPOINT = 'http://127.0.0.1:8000/auth/'
POST_ENDPOINT = 'http://127.0.0.1:8000/api/status/'

user = {
    "username": "rezasj78",
    "password": "sherlock761"
}

headers_1 = {
    'Content-type': 'application/json',
    # 'Authentication': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InJlemFzajc4IiwiZXhwIjoxNTg0MTg3Mzc4LCJlbWFpbCI6InNhaHJhZWlhbnJlemFAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1ODQxODcwNzh9.17mKBiZ7euqBGbcK9brlgbq4uJ6_41jZOi5Srwg6_gw'
}

res = requests.post(ENDPOINT, data=json.dumps(user), headers=headers_1)
print(res.status_code)
print(res.text)
token = res.json()['token']

headers_2 = {
    "Content-type": "application/json",
    'Authorization': 'JWT ' + token
}

res2 = requests.post(ENDPOINT, data=json.dumps(user), headers=headers_2)
print(res2.text)
