#!/usr/bin/python3
"""
This is module 1-hbnb_route.py

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
