#!/usr/bin/python3
from flask import Flask
"""
Script that starts a Flask web application
"""
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    Return a simple string for index page
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
