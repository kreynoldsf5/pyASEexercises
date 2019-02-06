from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver, json, pymongo
from bson import ObjectId

class ASEWebServer(BaseHTTPRequestHandler):
    def _respond(self, ResponseCode, ContentType):
        self.send_response(ResponseCode)
        self.send_header('Content-type', ContentType)
        self.end_headers()

    def _clean_doc(self, objID):
        doc = pyPOSTs.find_one({"_id": ObjectId(objID)})
        del doc["_id"]
        return doc 

    def do_index(self):
        r = open("index.html", "r")
        self.wfile.write(bytes(r.read(), "utf8"))
        self._respond(200, 'text/html')

    def do_data(self):
        reply = []
        for d in pyPOSTs.find():
            reply.append(self._clean_doc(d["_id"]))
        self.wfile.write(bytes(json.dumps(reply), 'utf8'))
        self._respond(200, 'text/json')

    def do_GET(self):
        if self.path == '/data':
            self.do_data()
        else:
            self.do_index()

    def do_POST(self):
        try:
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len).decode("UTF-8")
            data = json.loads(post_body)
            result = pyPOSTs.insert_one(data)
            self.wfile.write(bytes(json.dumps(self._clean_doc(result.inserted_id), 'utf8')))
            self._respond(200, 'text/json')
        except Exception as e:
            print("error: " + str(e))
            self.wfile.write(bytes(json.dumps(dict(error=str(e))), 'utf8'))
            self._respond(400, 'text/json')
            
def run():
  server_address = ('', 8181)
  httpd = HTTPServer(server_address, ASEWebServer)
  print('running http server...')
  httpd.serve_forever()
  
client = pymongo.MongoClient('mongodb://root:ASEexample@mongo-server')
pyPOSTs = client['ASEexample'].pyPOSTs
pyPOSTs.create_index([('name', pymongo.ASCENDING)], unique=True)
run()