#!/usr/bin/python3
'''flask app that prints hello worldls'''
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!ce'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)