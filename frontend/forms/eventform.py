from flask_wtf import FlaskForm
from wtforms import StringField,FileField
from wtforms.validators import InputRequired

class EventAdd(FlaskForm):
    name=StringField('Event Name',validators=[InputRequired()])
    org=StringField('Event Organiser',validators=[InputRequired()])
    date=StringField('Event Date',validators=[InputRequired()])
    time=StringField('Event Time',validators=[InputRequired()])
    venue=StringField('Event Venue',validators=[InputRequired()])
    
