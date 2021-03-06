from flask import jsonify
from app import app
from app.create_entry import entries


@app.route("/")
def hello():
    return "Welcome to my dairy application", 200


@app.route('/api/v1/entries')
def fetch_entries():
    return jsonify({'entries': entries}), 200
