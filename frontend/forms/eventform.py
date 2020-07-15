from flask_wtf import FlaskForm
from wtforms import StringField,FileField,DateField
from wtforms.validators import InputRequired

class EventAdd(FlaskForm):
    name=StringField('Event Name',validators=[InputRequired()])
    org=StringField('Event Organiser',validators=[InputRequired()])
    date=DateField('Event Date',format='%Y-%m-%d')
    time=StringField('Event Time',validators=[InputRequired()])
    venue=StringField('Event Venue',validators=[InputRequired()])
    
