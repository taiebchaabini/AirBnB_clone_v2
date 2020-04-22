#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import g
from models import storage
from models import State
"""
Script that starts a Flask web application
"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
        storage.close()


@app.route('/states_list')
def states_list():
    data = storage.all(State)
    states = []
    for k in data:
        states.append(data[k])
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
