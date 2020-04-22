#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import g
from models import storage
from models import State
from models import Amenity
"""
Script that starts a Flask web application
"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
        storage.close()


@app.route('/hbnb_filters')
def states_list(id=None):
    """
    Display a page for hbnb_filters
    State, City and Amenity objects must be loaded from DBStorage
    """
    data = storage.all(State)
    states = []
    for k in data:
        states.append(data[k])

    data = storage.all(Amenity)
    amenities = []
    for k in data:
        amenities.append(data[k])

    return render_template('10-hbnb_filters.html', states=states,
        amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
