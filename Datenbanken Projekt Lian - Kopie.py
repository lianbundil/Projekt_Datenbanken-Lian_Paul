from flask import Flask
from flask import render_template
from flask import request
import users

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello/<string:username>")
def hello_user(username):
    return f"<html><head></head><body>Hello <b>{username} </b></body></html>"

@app.route("/hello_flask")
def hello_flask():
    return render_template(
        "template.html",
        title="Hello Flask",
        description="This is my first website!")

@app.route("/hello_flask2")
def hello_flask2():
    return render_template(
        "template.html",
        title="Hello Flask 2",
        description="This is our website!")

@app.route("/hello_flask_football")
def hello_flask_football():
    return render_template(
        "template.html",
        title="Hello Flask Football",
        description="Welcher Spieler interessiert Dich?")

def hello_flask_football():
    return render_template(
       "template.html",
       title="Hello Flask Football",
        description="Gib seinen Namen hier ein hier ein:_______________________")


@app.route("/add_user", methods=["GET", "POST"])
def user_form():
    if request.method == "GET":
        return '''<form method="POST">
                      <div><label>Username: <input type="text" name="username"></label></div>
                      <div><label>Firstname: <input type="text" name="firstname"></label></div>
                      <div><label>Lastname: <input type="text" name="lastname"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        user = users.User(username, firstname, lastname)
        user.to_db()
        return f"User {username} was created"



