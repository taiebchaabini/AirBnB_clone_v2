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


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    data = storage.all(State)
    states = []
    if id is None:
        for k in data:
            states.append(data[k])
    else:
        id = 'State.' + id
        states = data.get(id)
    return render_template('9-states.html', states=states, id=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
