#!/usr/bin/python3
from flask import Flask
from flask import render_template
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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """
    display “Python ”, followed by the value of the text variable (replace
    underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    text = 'Python ' + text
    return text


@app.route('/number/<int:n>')
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    if (type(n) is int):
        return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n=None):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer
    """
    if (n % 2) == 0:
        ntype = "even"
    else:
        ntype = "odd"
    return render_template('6-number_odd_or_even.html', n=n, ntype=ntype)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
