from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your bio:',validators=[Required()])
    submit = SubmitField('Submit')
    