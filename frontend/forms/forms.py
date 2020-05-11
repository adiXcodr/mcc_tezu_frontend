from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired,Length

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[InputRequired(),Length(max=10,message="username too long")])
    password=PasswordField('Password',validators=[InputRequired()])
    recaptcha=RecaptchaField()

