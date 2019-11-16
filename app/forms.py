from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class DetailForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('name', validators=[DataRequired()])  # todo - validate unique
    val = StringField('value')
    submit = SubmitField('Submit')
