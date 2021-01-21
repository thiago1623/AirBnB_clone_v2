#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_given_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all("State")
    found_state = ""
    for s_id in states:
        if s_id == id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    """Displays an HTML page with info about <id>, if it exists."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
