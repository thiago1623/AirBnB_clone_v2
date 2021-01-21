#!/usr/bin/python3

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """script that starts a Flask"""
    all_info = {}
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    for state in states:
        all_info[state.name] = state

    return render_template('10-hbnb_filters.html',
                           states=all_info,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(err):
    """script that starts a Flask"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
