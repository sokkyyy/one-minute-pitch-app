from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, StringField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write your bio:',validators=[Required()])
    submit = SubmitField('Submit Bio')


class PitchForm(FlaskForm):
    category = SelectField('Pitch Category:', 
                choices=[('general','General Pitch'),('product', 'Product Pitch'),('fashion','Fashion Pitch'),('interview','Interview Pitch')],
                validators=[Required()])
    details = TextAreaField('Enter your one minute pitch:',validators=[Required()])
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment on the Pitch:',validators=[Required()])
    submit = SubmitField('Submit Comment')