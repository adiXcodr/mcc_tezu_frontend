from flask import Blueprint,render_template
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

@usr.route("/notifications")
def notifications():
    notifications=requests.get("https://mcctezu-backend.herokuapp.com/run-model/notifications/fetch").json()      
    return render_template("notifications.html",notifications=notifications["data"])
@usr.route("/notifications",methods=["POST"])
def add_notifications():
    id=request.form['id']
    title=request.form['title']
    text=request.form['text']
    DT = datetime.datetime.now()
    currentDT=datetime.date.isoformat(DT)
    res=requests.post("https://mcctezu-backend.herokuapp.com/run-model/notifications/add",json={"_id":int(id),"date":currentDT,"title":title,"notification":text})
    return notifications()

@usr.route("/notifications/",methods=["POST"])
def delete_notifications():
    id=request.form['id']
    print(id)
    res=requests.delete("https://mcctezu-backend.herokuapp.com/run-model/notifications/delete_one",json={"_id":int(id)})
    print(res)
    return notifications()
@usr.route("/notifications/update",methods=["POST"])
def update_notifications():
    id=request.form['id']
    date=request.form['date']
    title=request.form['title']
    text=request.form['text']
    res=requests.put("https://mcctezu-backend.herokuapp.com/run-model/notifications/update",json={"_id":int(id),"date":str(date),"title":str(title),"notification":str(text)})
    print(res)
    return notifications()


@usr.route("/our-services")
def our_services():
    return render_template("our-services.html")

@usr.route("/publications")
def publications():
    return render_template("publications.html")