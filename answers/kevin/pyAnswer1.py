#!/usr/bin/env python
import requests

url = 'http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com'
r = requests.get(url)
print(r.text)