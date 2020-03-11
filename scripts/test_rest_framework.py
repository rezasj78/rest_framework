import requests
import json
import os

# ENDPOINT = 'http://127.0.0.1:8000/api/status/all/'
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json is True:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
# data = {
#     "user": 2,
#     "content": "new content",
#     "img": None,
#     "id": 10
# }
# do(method='delete', data=data)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASE_DIR, 'db.sqlite3')
print(BASE_DIR)