
import os
import requests
from flask import Flask,render_template,request,jsonify
import datetime
 


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
    notifications=requests.get("https://mcctezu-backend.herokuapp.com/run-model/notifications/fetch").json()        
    return render_template("notifications.html",notifications=notifications["data"])

@app.route("/our-services")
def our_services():
    return render_template("our-services.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/notifications",methods=["POST"])
def add_notifications():
    id=request.form['id']
    title=request.form['title']
    text=request.form['text']
    DT = datetime.datetime.now()
    currentDT=datetime.date.isoformat(DT)
    res=requests.post("https://mcctezu-backend.herokuapp.com/run-model/notifications/add",json={"_id":id,"date":currentDT,"title":title,"notification":text})
    return notifications()

"""
@app.routes("/admin")
    return render_template("admin-login.html")
"""
if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        index()





