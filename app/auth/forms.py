from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User 

class RegistrationForm(FlaskForm):
    email = StringField('Email:',validators=[Required(),Email()])
    username = StringField('Username:',validators=[Required()])
    password = PasswordField('Password:',validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm your Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        '''
        validate _ runs with the other validators.
        '''
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email.')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username is already taken.')

class LoginForm(FlaskForm):
    