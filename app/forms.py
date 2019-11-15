from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class DetailForm(FlaskForm):
    id = HiddenField('id', render_kw={'primary_key': True})
    name = StringField('name', validators=[DataRequired()])  # todo - validate unique
    val = StringField('value')
    submit = SubmitField('Submit')
