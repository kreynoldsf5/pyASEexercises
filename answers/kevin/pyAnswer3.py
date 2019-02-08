#!/usr/bin/env python
import requests
import json

def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key] == value]

url = "http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com/data"
r = requests.get(url)
pyResponse = json.loads(r.text)
result = search_dictionaries("name", "tee", pyResponse)
print(result[0]["message"])
