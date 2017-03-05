from flask import Flask, request, redirect
from flask_socketio import SocketIO
import os
from pymongo import MongoClient

DB_USER = 'dev'
DB_PASS = 'python'

client = MongoClient("mongodb://{}:{}@ds050879.mlab.com:50879/peopleseen".format(DB_USER, DB_PASS))

# db = client.test_database

# collection = db.test_collection

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
      socketio.debug = True
    socketio.run(app)
