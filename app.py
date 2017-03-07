import os
from flask import Flask, request, redirect
from flask_socketio import SocketIO
from pymongo import MongoClient

DB_USER = "dev"
DB_PASS = "python"

client = MongoClient("mongodb://{}:{}@ds157248.mlab.com:57248/flashtag".format(DB_USER, DB_PASS))

db = client.test

collection = db.test

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=['GET'])
def index():
    return "Hello World"

@socketio.on('connection')
def connection(message):
    print "Connect!"
    valid = false
    if message.connecting:
      valid = true
    data = []
    emit('connection_response', {
      'valid': valid,
      'data': data
    })


@socketio.on('map_get')
def map_get(message):
    # From message take in location
    valid = false
    if message.location:
        valid = true
    # Query DB for places near that location
    data = []
    # return all things near
    emit('map_response', {
      'valid': valid,
      'data': data
    })


@socketio.on('marker')
def connection(message):
    valid = false
    # From message take in ID
    if message.marker:
      valid = true
    # Query DB for ID of marker
    data = []
    # Return Marker data
    emit('marker_response', {
      'valid': valid,
      'data': data
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print "Magic Happening on port: {}".format(port)
    socketio.run(app)
