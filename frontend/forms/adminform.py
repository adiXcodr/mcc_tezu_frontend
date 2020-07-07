import requests
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,ValidationError
from wtforms.validators import InputRequired,Length,EqualTo

class AdminAdd(FlaskForm):
    fullname=StringField('Fullname',validators=[InputRequired()])
    username=StringField('Username',validators=[InputRequired()])
    password=PasswordField('Password',validators=[InputRequired(),Length(min=8),EqualTo('confirm')])
    confirm=PasswordField('Confirm Password',validators=[InputRequired()])

    #CUSTOM VALIDATOR FOR USERNAME
    def validate_username(FlaskForm,username):
        url="http://mcctezu-backend.herokuapp.com/run-model/admin-view/{}"
        req=requests.get(url.format(username.data)).json()
        if req["status"]!="Failure":
            raise ValidationError("Username Already Taken!")
