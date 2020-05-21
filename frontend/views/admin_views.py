import datetime
import requests
from flask import Blueprint,render_template,request,json,session,flash,jsonify,redirect,url_for
from passlib.hash import pbkdf2_sha256
from frontend import app
from frontend.forms.forms import LoginForm
from frontend.forms.eventform import EventAdd
from frontend.forms.adminform import AdminAdd
from frontend.forms.ntfform import NotificationAdd
admin=Blueprint("admin",__name__)
#http://mcctezu-backend.herokuapp.com/
@admin.route("/admin",methods=['POST','GET'])
def admin_login():
    form=LoginForm()
    if session.get("ID",None) is not None:
        return redirect(url_for("admin.admin_dash"))
    elif form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        url="http://mcctezu-backend.herokuapp.com/run-model/admin-view/{}"
        req=requests.get(url.format(form.username.data)).json()
        if req["status"]=='Success':
            hsh=req["result"][0]["password"]
            if pbkdf2_sha256.verify(password,hsh):
                session['ID']=req["result"][0]["fullname"]
                return redirect(url_for("admin.admin_dash"))
            flash('username or password is incorrect','danger')
    return render_template('admin-login.html',form=form)
@admin.route('/admin-dash',methods=['GET'])
def admin_dash():
    form1=EventAdd()
    form2=NotificationAdd()
    form4=AdminAdd()
    if session.get('ID',None) is not None:
        req_evt=requests.get("http://mcctezu-backend.herokuapp.com/run-model/get_events").json()
        req_ntf=requests.get("https://mcctezu-backend.herokuapp.com/run-model/notifications/fetch").json()
        req_adm=requests.get("http://mcctezu-backend.herokuapp.com/run-model/admin-view").json()
        events=req_evt["result"]
        notifications=req_ntf["data"]
        admin=req_adm["result"]
        return render_template('admin-dash.html',evt=form1,ntf=form2,adm=form4,events=events,notifications=notifications,admin=admin)
    return redirect(url_for('admin.admin_login'))
@admin.route('/admin-logout',methods=['POST','GET'])
def admin_logout():
    if session.get('ID',None) is not None:
        session.pop('ID')
        return redirect(url_for('admin.admin_login'))
    flash('Login First','warning')
    return redirect(url_for('admin.admin_login'))

#---------ADMIN EVENTS HANDLER-------------
@admin.route('/admin-add-event',methods=['POST'])
def admin_add_event():
    form=EventAdd()
    url="http://mcctezu-backend.herokuapp.com/run-model/add_events"
    if session.get("ID",None) is not None:
        if form:
            name=form.name.data
            org=form.org.data
            date=form.date.data
            time=form.time.data
            venue=form.venue.data
            f=request.files.get('image')
            req=requests.post(url,files=f,json={"evt_name":name,"evt_org":org,"evt_date":date,"evt_time":time,"evt_venue":venue,"evt_image":"null"}).json()
            res=req["status"]
            return redirect(url_for('admin.admin_dash',res=res))
        return redirect(url_for('admin.admin_dash'))
    return redirect(url_for('admin.admin_login'))
@admin.route('/admin-delete-event/<name>',methods=['GET'])
def admin_delete_event(name):
    if session.get("ID",None) is not None:
        url="http://mcctezu-backend.herokuapp.com/run-model/delete_events"
        req=requests.delete(url,json={"evt_name":name}).json()
        res=req["status"]
        return redirect(url_for('admin.admin_dash',res=res))
    return redirect(url_for('admin.admin_login'))
@admin.route('/view/<filename>',methods=['GET'])
def view_image(filename):
    req=requests.get("http://mcctezu-backend.herokuapp.com/run-model/get-img/{}".format(filename=filename))
    return req.text
@admin.route("/admin-add-notifications",methods=["POST"])
def add_notifications():
    id=request.form['id']
    title=request.form['title']
    text=request.form['description']
    DT = datetime.datetime.now()
    currentDT=datetime.date.isoformat(DT)
    res=requests.post("https://mcctezu-backend.herokuapp.com/run-model/notifications/add",json={"_id":int(id),"date":currentDT,"title":title,"notification":text})
    return redirect(url_for('admin.admin_dash'))

@admin.route('/admin-delete-notification/<int:id>')
def delete_notifications(id):
    print(id)
    res=requests.delete("https://mcctezu-backend.herokuapp.com/run-model/notifications/delete_one",json={"_id":int(id)})
    print(res)
    return redirect(url_for('usr.notifications'))
@admin.route("/admin-update-notifications",methods=["POST"])
def update_notifications():
    id=request.form['id']
    date=request.form['date']
    title=request.form['title']
    text=request.form['description']
    res=requests.put("https://mcctezu-backend.herokuapp.com/run-model/notifications/update",json={"_id":int(id),"date":str(date),"title":str(title),"notification":str(text)})
    print(res)
    return redirect(url_for('usr.notifications'))