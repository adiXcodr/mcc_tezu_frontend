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
#https://mcctezu-backend.herokuapp.com/
@admin.route("/admin",methods=['POST','GET'])
def admin_login():
    form=LoginForm()
    if session.get("ID",None) is not None:
        return redirect(url_for("admin.admin_dash"))
    elif form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        url="https://mozcctuapi.herokuapp.com/run-model/admin-view-check/{}"
        req=requests.get(url.format(form.username.data)).json()
        if req["status"]=='Success':
            hsh=req["result"][0]["password"]
            print(hsh)
            if pbkdf2_sha256.verify(password,hsh):
                session['ID']=req["result"][0]["username"]
                return redirect(url_for("admin.admin_dash"))
            flash('username or password is incorrect','danger')
    return render_template('admin-login.html',form=form)

@admin.route('/admin-dash',defaults={'res':'n'},methods=['GET'])
@admin.route('/admin-dash/<res>',methods=['GET'])
def admin_dash(res):
    form1=EventAdd()
    form2=NotificationAdd()
    form4=AdminAdd()
    if session.get('ID',None) is not None:
        req_evt=requests.get("https://mozcctuapi.herokuapp.com/run-model/event").json()
        req_ntf=requests.get("https://mozcctuapi.herokuapp.com/run-model/notifications/fetch").json()
        req_adm=requests.get("https://mozcctuapi.herokuapp.com/run-model/admin-view").json()
        events=req_evt["result"]
        notifications=req_ntf["data"]
        admin=req_adm["result"]
        return render_template('admin-dash.html',evt=form1,ntf=form2,adm=form4,events=events,notifications=notifications,admin=admin,res=res)
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
    evt=EventAdd()
    url="https://mozcctuapi.herokuapp.com/run-model/event"
    if session.get("ID",None) is not None:
        if evt.validate_on_submit():
            name=evt.name.data
            org=evt.org.data
            date=evt.date.data
            time=evt.time.data
            venue=evt.venue.data
            date=str(date)
            req=requests.post(url,json={"evt_name":name,"evt_org":org,"evt_date":date,"evt_time":time,"evt_venue":venue,"evt_image":"null"}).json()
            res=req["status"]
            return redirect(url_for('admin.admin_dash',res=res))
        return redirect(url_for('admin.admin_dash',res='Failure'))
    return redirect(url_for('admin.admin_login'))
@admin.route('/admin-delete-event/<int:id>',methods=['GET'])
def admin_delete_event(id):
    if session.get("ID",None) is not None:
        req=requests.delete("https://mozcctuapi.herokuapp.com/run-model/event",json={"id":id}).json()
        res=req["status"]
        return redirect(url_for('admin.admin_dash',res=res))
    return redirect(url_for('admin.admin_login'))
@admin.route('/admin-update-event/<int:id>',methods=['POST'])
def admin_update_event(id):
    form=EventAdd()
    if session.get("ID",None) is not None:
        if form:
            url="https://mozcctuapi.herokuapp.com/run-model/event"
            evt_name=form.name.data
            evt_org=form.org.data
            evt_date=str(form.date.data)
            evt_time=form.time.data
            evt_venue=form.venue.data
            param={"field":{"id":id},"field_update":{"evt_name":evt_name,"evt_org":evt_org,"evt_date":evt_date,"evt_time":evt_time,"evt_venue":evt_venue}}
            req=requests.put(url,json=param)
            res=req.status
            return redirect(url_for('admin.admin_dash',res=res))
        return redirect(url_for('admin.admin_dash',res='Failure'))
    return redirect(url_for('admin.admin_login'))

@admin.route('/view/<filename>',methods=['GET'])
def view_image(filename):
    req=requests.get("https://mozcctuapi.herokuapp.com/run-model/get-img/{}".format(filename=filename))
    return req.text

#-----------------------NOTIFICATIONS------------------------
@admin.route("/admin-add-notifications",methods=["POST"])
def add_notifications():
    ntf=NotificationAdd()
    if session.get('ID',None) is not None:
        if ntf.validate_on_submit():
            id=request.form['id']
            title=request.form['title']
            text=request.form['description']
            DT = datetime.datetime.now()
            currentDT=datetime.date.isoformat(DT)
            req=requests.post("https://mozcctuapi.herokuapp.com/run-model/notifications/add",json={"_id":int(id),"date":currentDT,"title":title,"notification":text}).json()
            res=req['status']
            return redirect(url_for('admin.admin_dash',res=res))
        return redirect(url_for('admin.admin_dash',res='Failure'))
    return redirect(url_for('admin.admin_login'))

@admin.route('/admin-delete-notification/<int:id>')
def admin_delete_notifications(id):
    if session.get("ID",None) is not None:
        req=requests.delete("https://mozcctuapi.herokuapp.com/run-model/notifications/delete_one",json={"_id":int(id)}).json()
        res=req["status"]
        return redirect(url_for('admin.admin_dash',res=res))
    return redirect(url_for('admin.admin_login')) 
@admin.route("/admin-update-notifications",methods=["POST"])
def update_notifications():
    if session.get("ID",None) is not None:
        id=request.form['id']
        date=request.form['date']
        title=request.form['title']
        text=request.form['description']
        req=requests.put("https://mozcctuapi.herokuapp.com/run-model/notifications/update",json={"_id":int(id),"date":str(date),"title":str(title),"notification":str(text)}).json()
        res=req["status"]
        return redirect(url_for('admin.admin_dash',res=res))
    return redirect(url_for('admin.admin_login'))

#-------------------------ADMIN------------------------------
@app.route('/admin-add-one',methods=['POST'])
def admin_add_one():
    adm=AdminAdd()
    if session.get('ID',None) is not None:
        if adm.validate_on_submit():
            fullname=adm.fullname.data
            username=adm.username.data
            password=adm.password.data
            req=requests.post("https://mozcctuapi.herokuapp.com/run-model/admin-add",json={"fullname":fullname,"username":username,"password":password}).json()
            res=req["status"]
            return redirect(url_for('admin.admin_dash',res=res))
        return redirect(url_for('admin.admin_dash',res='Failure'))
    return redirect(url_for('admin.admin_login'))
@app.route('/admin-delete/<uname>')
def admin_delete(uname):
    if session.get('ID',None) is not None:
        req=requests.delete("https://mozcctuapi.herokuapp.com/run-model/admin-remove",json={"username":uname}).json()
        res=req["status"]
        return redirect(url_for('admin.admin_dash',res=res))
    return redirect(url_for('admin.admin_login'))

