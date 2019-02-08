# Exercise 1

_Goal:_ Create an HTTP GET request and display(_print()_) the results.

Python has an extremely useful socket library to deal with system networking and a rich collection of modules built on top of those libraries. When interacting with a RESTful API with Python, its extremely common to use the [requests](https://github.com/requests/requests) library (it's one of the few libs included with the Python installation on BIG-IP). We'll use this library for today's exercises.

The Requests library is well [documented](http://docs.python-requests.org/en/master/) including specific [examples](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request). Please take a few minutes to read through the documentation.

The target web server is currently deployed in AWS at [http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com](http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com). For this exercise, make an HTTP GET request to the root (/). Feel free to use the Python interpreter (per the documentation examples) for working out the exercise but please create executable scripts for your exercise answers (for easier sharing).

Let me get you started.

```python
#!/usr/bin/env python
import requests

###your code here###
```

<details><summary>Interactive Solution</summary>
<p>

![Exercise1](./gifs/pyExercise1.gif)
      
</p>
</details>

[Move on to Exercise 2](./pyExercise2.md)

[Return to the README.md](./README.md)
