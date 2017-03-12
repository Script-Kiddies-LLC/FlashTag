import os
from flask import Flask, request, redirect
from flask_socketio import SocketIO
from pymongo import MongoClient

client = MongoClient()

db = client.flashtag

collection = db.test

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=['GET'])
def index():
    return "Hello World"

@socketio.on('connect')
def connection(message):
    valid = false
    if message.connecting:
      valid = true
    data = collection.find()
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
    data = collection.find()
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
    data = collection.find()
    # Return Marker data
    emit('marker_response', {
      'valid': valid,
      'data': data
    })

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == "__main__":
    socketio.run(app, debug = True)
