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


@app.route('/hbnb')
def hbnb():
    """
    Return a simple string for hbnb page
    """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """
    display “C ” followed by the value of the text variable (replace underscore
    _ symbols with a space )
    """
    text = text.replace('_', ' ')
    text = 'C ' + text
    return text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
