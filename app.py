from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
      app.debug = True
    app.run(host='0.0.0.0', port=port)
