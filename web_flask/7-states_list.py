#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage."""
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
