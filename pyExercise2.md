# Exercise 2

_Goal:_ Create an HTTP POST request which posts your name and a message. 

Our web application expects a [JSON](https://www.json.org/) payload which, minimally, should include a 'name' and a 'message' property. A valid response from the webserver will echo your request payload back in the HTTP response body.

```json
{
    "name": "kevin",
    "message": "this is an example POST"
}
```

## JSON encoding

Recall the various data types in Python. Here is a mapping of Python data types to [JSON object types](https://www.json.org/).


| Python           | JSON   |
|------------------|--------|
| dict	           | object |
| list, tuple	   | array  |
| str	           | string |
| int, long, float | number |
| True	           | true   |
| False	           | false  |
| None	           | null   |

The Python [json](https://docs.python.org/3/library/json.html) library can be used to easily create JSON strings from Python data types (_json.dumps()_) and create Python data types from JSON strings (_json.loads()_). What Python data type is your request payload (and a successful response body)? 

In this example, we'll start with a Python data structure (a dictionary) and we'll finish with a JSON string.
![Example1](./gifs/pyExample1.gif)

Note the subtle differences between these objects.
```python
>>> data
{'name': 'kevin', 'message': 'this is a message'}
>>> type(data)
<class 'dict'>
>>> dataJSON = json.dumps(data)
>>> dataJSON
'{"name": "kevin", "message": "this is a message"}'
>>> type(dataJSON)
<class 'str'>
```

### POSTing Payload

Now that we know how to generate JSON from python data structures, we need to pass that data as a POST payload. The Python _Requests_ library documentation provides sufficient [examples](http://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests).

```python
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))
```

In later versions of the Python _Requests_ library JSON encoding is natively supported (but deserialization, _json.loads()_, is still a valuable skill).

```python
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)
```

### Putting it all together

Now we simply need to:
* Create our payload
* Send the POST
* Validate the response

Prepare your script. Note that each entry in the database *must* have a unique name. Please let me know if you need an entry removed.

<details><summary>Interactive Solution</summary>
<p>

![Exercise2](./gifs/pyExercise2.gif)
      
</p>
</details>

[Move on to Exercise 3](./pyExercise3.md)

[Return to the README.md](./README.md)