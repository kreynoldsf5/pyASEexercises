# Notes

* Mongo shell example
```bash
root@8e6db679d80e:/# mongo mongodb://root:ASEexample@mongo-server
MongoDB shell version v4.0.6
connecting to: mongodb://mongo-server:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("071aebde-7693-4f56-8310-3999eb0f976a") }
MongoDB server version: 4.0.6
Server has startup warnings: 
2019-02-07T01:55:58.277+0000 I STORAGE  [initandlisten] 
2019-02-07T01:55:58.277+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-02-07T01:55:58.278+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
---
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---

> use ASEexample
switched to db ASEexample
> db.pyPOSTs.find().pretty()
{
	"_id" : ObjectId("5c5b8eaa29f8ea0001ad4ae4"),
	"name" : "kevin",
	"message" : "this is an example POST"
}
> db.pyPOSTs.remove({"name": "kevin"})
WriteResult({ "nRemoved" : 1 })
```

```json
[
	{ "name": "Author", "message": "vaguely remembering something about a bypass" },
	{ "name": "Ford", "message": "bring your towel" },
	{ "name": "Marvin", "message": "I'm not feeling well." }
]
```

```python
def search_dictionaries(key, value, list_of_dictionaries):
    [return element for element in list_of_dictionaries if element[key] == value]
```