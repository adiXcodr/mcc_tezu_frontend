import datetime
import requests
from flask import Blueprint,render_template,redirect,url_for,request
from frontend.forms.eventform import EventAdd
usr=Blueprint("usr",__name__)

@usr.route("/")
def index():
    return render_template("index.html")

@usr.route("/contacts")
def contacts():
    return render_template("contacts.html")

@usr.route("/events")
def add_event():
    return render_template("events.html")
@usr.route("/members")
def members():
    return render_template("members.html")
@usr.route("/our-services")
def our_services():
    return render_template("our-services.html")

@usr.route("/notifications")
def notifications():
    
    return render_template("notifications.html")

@usr.route("/publications")
def publications():
    return render_template("publications.html")