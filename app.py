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

@socketio.on('connection')
def connection(message):
    emit('connection_response', {'valid': false})

@socketio.on('map_get')
def map_get(message):
    # From message take in location
    # Query DB for places near that location
    # return all things near
    emit('map_response', {'valid': false})

@socketio.on('marker')
def connection(message):
    # From message take in ID
    # Query DB for ID of marker
    # Return Marker data
    emit('marker_response', {'valid': false})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
      socketio.debug = True
    socketio.run(app)
