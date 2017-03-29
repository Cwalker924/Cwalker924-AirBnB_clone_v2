#!/usr/bin/python3
"""
This is module 6-number_odd_or_even.py

This module starts a web aplication via Flask
"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>")
def num(n):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_template(n):
        return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd(n):
        return (render_template("6-number_odd_or_even.html", n=n))

if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
