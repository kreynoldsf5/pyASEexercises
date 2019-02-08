#!/usr/bin/env python
import requests
import json

payload = dict()
payload['name'] = "not kevin"
payload['message'] = "not the same message"
url = "http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com"
r = requests.post(url, data=json.dumps(payload))
print(r.status_code)
print(r.text)


###your code here###