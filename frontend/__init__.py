import os
from flask import Flask
from .config import Development,Production
app = Flask(__name__)

#ADDING CONFIGURATIONS
app.config.from_object(Production())

#IMPORTS TO REGISTER BLUEPRINTS
from frontend.views.admin_views import admin
from frontend.views.usr_views import usr

#REGISTERING BLUEPRINT
app.register_blueprint(admin)
app.register_blueprint(usr)