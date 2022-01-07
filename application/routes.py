from application import app
from flask import jsonify

@app.route("/")
def index():
    return jsonify({ "result":"Ola!" }), 400