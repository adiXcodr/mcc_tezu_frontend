import os
from flask import Flask
app = Flask(__name__)

#ADDING CONFIGURATIONS
app.config['SECRET_KEY']='text'
app.config['RECAPTCHA_PUBLIC_KEY']='6LeLZPEUAAAAADqu8vW2IEam3ZjgsLot11Uhe9EP'
app.config['RECAPTCHA_PRIVATE_KEY']='6LeLZPEUAAAAAHjeIVUeVOqcrVXLsSMOOPjT7_Fy'

#IMPORTS TO REGISTER BLUEPRINTS
from frontend.views.admin_views import admin
from frontend.views.usr_views import usr

#REGISTERING BLUEPRINT
app.register_blueprint(admin)
app.register_blueprint(usr)