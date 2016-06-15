#!/usr/bin/env python3

#Import packages
from flask import *
import sqlite3

#Start flask app
app = Flask(__name__)

#Default index page
@app.route('/')
def hello_word():
    return "Welcome to Benja World!"

#The town page, the game will automatically direct the page to your town when accesing this URL
@app.route('/town/')
def showTown():
    return render_template("town.html")

@app.route('/group/')
def showGroup():
    return render_template("group.html")

@app.route('/g/<username>')
def show_user(username):
    return "This is the group of: " + username

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
