#!/usr/bin/env python3
from flask import *
app = Flask(__name__)

#Default index page
@app.route('/')
def hello_word():
    return "Hello, World!"

#The town page, the game will automatically direct the page to your town when accesing this URL
@app.route('/town/')
def showTown():
    return render_template("town.html")

@app.route('/t/<username>')
def show_user(username):
    return "Hello, World! " + username

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
