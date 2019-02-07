
# ASE Python Exercises

Python is an extremely common language throughout organizations -- but especially with Network Operations (NetOps) teams. Before these exercises are attempted you should have completed the provided Python training from [Code Academy](https://www.codecademy.com/learn/learn-python-3). 

NetOps Python use cases commonly involve interacting with RESTful APIs. These exercises focus on making HTTP requests and manipulating response data using the Python _Requests_ library. 

## Overview

First, verify that you have proper environment to perform the exercises. Python3 should be [installed](./pyEnvSetup.md) on your machine. A text editor with IDE functionality would also be useful ([Visual Studio Code](https://code.visualstudio.com/), [Sublime Text](https://www.sublimetext.com/), [Notepad++](https://notepad-plus-plus.org/), etc).

Secondly, we'll do a [lightening round overview](./pyOverview.md) of the content from the learning path. We'll briefly touch on the fundamental concepts from the self-study.

_15 min_

## Exercises

These exercises will focus on creating HTTP requests in Python. We'll build upon this exercise for our JavaScript review next week.

I've written a small web server with a database backend (mongoDB) in Python (~50 lines). The [app](./WebServer/app.py) is packaged in two docker containers and can be easily built/run on any docker host. 

The webserver will respond in accordance to this table:

| Method | Path  | Result      |
|--------|-------|-------------|
| GET    | /*    | index.html  |
| GET    | /data | db contents |
| POST   | /*    | db insert   |

### Exercise Overviews

For each exercise, I have provided a solution based on running python interactively. Please package your answers in scripts so they can be easily shared.
```python
#!/usr/bin/env python
import requests

###your code here###
```

<details><summary>Optional</summary>
<p>

If you are comfortable with git, clone the repo, create a branch, and collect your answers in directory under the [answers](./answers) directory of the repository. Initiate a [pull request](https://help.github.com/articles/about-pull-requests/) when you're done.
      
</p>
</details>

#### [Exercise 1](./pyExercise1.md)

Craft a GET request to / and *print()* the returned html.

_10min_

#### [Exercise 2](./pyExercise2.md)

Send a POST containing the necessary JSON properties to store some data in the database.

_10min_

#### [Exercise 3](./pyExercise3.md)

Return the contents of the database (GET to /data) and store as the appropiate Python data structure. Perform some rudimentary data manipulation.

_15min_

<details><summary>Optional Advanced Exercises</summary>
<p>

Update the WebServer, [app.py](./WebServer/app.py) to be a little more useful. Here are some ideas:
Display a proper error page when recieving requests for paths that don't exist.
```bash
$ curl http://example.app/foo
HTTP/1.0 404 NOT FOUND
```
Implement a URI routing scheme that displays individual database entries based on path.
```bash
$ curl http://example.app/kevin
{'name': 'kevin', 'message': 'calmer than you are'}
HTTP/1.0 200 OK
```
Implement the DELETE http method to remove an individual record.
```bash
$ curl -X DELETE http://example.app/kevin
{'response': 'db entry "kevin" deleted'}
HTTP/1.0 200 OK
```
Or any other modification you want.
      
</p>
</details>


[Start on Exercise 1.](./pyExercise1.md)

