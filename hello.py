from flask import Flask
from gevent.pywsgi import WSGIServer
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") #indent this line
 
if __name__ == "__main__":
 http_server = WSGIServer(('', 8080), app)
 http_server.serve_forever()
 #app.run(host='0.0.0.0', port='8080') # indent this line
 
