#!/usr/bin/env python3

#Import packages
from flask import *

#Import local packages
import dbHandler

#Start flask app
app = Flask(__name__)

#Default index page
@app.route('/')
def showStart():
    return "Welcome to Benja World!"

#The town page, the game will automatically direct the page to your town when accesing this URL
@app.route('/login/')
def showLogin():
    return render_template("login.html")

#The town page, the game will automatically direct the page to your town when accesing this URL
@app.route('/town/')
def showTown():
    return render_template("town.html")

@app.route('/group/')
def showGroup():
    return render_template("group.html")

@app.route('/g/<username>')
def showUser(username):
    return "This is the group of: " + username

if __name__ == "__main__":
    #Initailize the database
    dbHandler.init("./database/")
    dbHandler.newGroup("dankMemeMan")
    dbHandler.end()
    app.run(debug=False, host="0.0.0.0")
