#!/usr/bin/python3
''' a flask app that prints hbnb '''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyt(text='is_cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    if type(n) is int:
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
