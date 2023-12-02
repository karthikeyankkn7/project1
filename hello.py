from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") #indent this line
if __name__ == "__main__":
 from waitress import serve
 serve(app, host="0.0.0.0", port=8080)
  #app.run(host='0.0.0.0', port='8080') # indent this line
 
