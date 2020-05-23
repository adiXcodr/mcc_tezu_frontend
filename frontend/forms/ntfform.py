from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired,Length

class NotificationAdd(FlaskForm):
    id=IntegerField('id',validators=[InputRequired()])
    title=StringField('Title',validators=[InputRequired()])
    description=StringField('Description',validators=[InputRequired(),Length(max=150)])