import requests
from flask import Blueprint,render_template,json,session,flash,jsonify,redirect,url_for
from passlib.hash import pbkdf2_sha256
from frontend import app
from frontend.forms.forms import LoginForm
from frontend.forms.eventform import EventAdd
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
    form=EventAdd()
    if session.get('ID',None) is not None:
        return render_template('admin-dash.html',form=form,res='n')
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
    url="http://mcctezu-backend.herokuapp.com/run-model/add-events"
    if session.get("ID",None) is not None:
        if form.validate_on_submit():
            name=form.name.data
            org=form.org.data
            date=form.date.data
            time=form.time.data
            venue=form.venue.data
            upload={"evt_name":name,"evt_org":org,"evt_date":date,"evt_time":time,"evt_venue":venue,"evt_image":null}
            req=requests.post(url,json=jsonify(upload))
        return redirect(url_for('admin.admin_dash'))
    return redirect(url_for('admin.admin_login'))