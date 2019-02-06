
# ASE Python Exercises

Python is an extremely common language throughout organizations -- but especially with Network Operations (NetOps) teams. Before these exercises are attempted, you should have completed the provided Python training from [Code Academy](https://www.codecademy.com/learn/learn-python-3).

## [Overview](./pyOverview.md)

First, we'll do a lightening round overview of the content from the learning path. We'll briefly touch on the fundamental concepts from the self-study.

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

#### [Exercise 1](./pyExercise1.md)

Craft a GET request to / and ***print()*** the returned html.

_10min_

#### [Exercise 2](./pyExercise2.md)

Send a POST containing the necessary JSON properties to store some data in the database.

_10min_

#### [Exercise 3](./pyExercise3.md)

Return the contents of the database (GET to /data) and store as the appropiate Python data structure. Perform some rudimentary data manipulation.

_15min_

#### Extra Credit

Update app.py to be a little more useful. Here are some ideas:
* Display a proper error page when recieving requests for paths that don't exist.
```bash
$ curl http://example.app/foo
HTTP/1.0 404 NOT FOUND
```
* Implement a URI routing scheme that displays individual database entries based on path.
```bash
$ curl http://example.app/kevin
{'name': 'kevin', 'message': 'calmer than you are'}
HTTP/1.0 200 OK
```
* Implement the DELETE http method to remove an individual record.
```bash
$ curl -X DELETE http://example.app/kevin
{'response': 'db entry "kevin" deleted'}
HTTP/1.0 200 OK
```
* Any other modification you want.



