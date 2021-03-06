#!/usr/bin/env python3

#Import packages
from flask import *

#Import local packages
import dbHandler as db

#Start flask app
app = Flask(__name__)

#Default index page
@app.route('/')
def showStart():
    return render_template("index.html")

#The town page, the game will automatically direct the page to your town when accesing this URL
@app.route('/login/')
def showLogin():
    resp = make_response(render_template("login.html"))
    resp.cache_control.no_cache = True
    return resp

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

#Post requests
@app.route('/login/', methods=['POST'])
def login():
    print("lel")
    db.newGroup(str(request.json["userID"]))
    print(request.json)
    return "Login: "

if __name__ == "__main__":
    #Initailize the database
    db.init("./database/")
    #db.end()
    app.run(debug=True, host="0.0.0.0")
