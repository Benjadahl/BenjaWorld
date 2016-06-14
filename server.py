#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello, World!"

@app.route('/user/<username>')
def show_user(username):
    return "Hello, World! " + username

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
