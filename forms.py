from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PlagForm(FlaskForm):
  checkText = TextAreaField('Enter your text here',validators=[DataRequired()])
  submit = SubmitField('Submit')
