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


@app.route('/python/<text>')
def pyt(text='is_cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
