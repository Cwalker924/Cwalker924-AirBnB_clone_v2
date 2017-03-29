#!/usr/bin/python3
"""
This is module 3-python_route.py

This module starts a web aplication via Flask
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
        return ("Hello HBNB!")


@app.route("/hbnb")
def hello_hbnb():
        return ("HBNB")


@app.route("/c/<text>")
def hello_c(text):
        text = text.replace("_", " ")
        return ("C {}".format(text))


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>")
def hello_python(text="is cool"):
        text = text.replace("_", " ")
        return ("Python {}".format(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
