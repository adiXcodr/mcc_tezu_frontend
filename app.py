
import os
import requests
from flask import Flask,render_template,request,jsonify


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/our-services")
def our_services():
    return render_template("our-services.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

"""
@app.routes("/admin")
    return render_template("admin-login.html")
"""
if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        index()





