from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    Class to instatiate user objects.
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255)) 
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        '''
        Function that will help in debugging
        '''
        return f'User {self.username}'




class Pitch(db.Model):
    '''
    Class to define the pithces made in the app
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_category = db.Column(db.String)
    pitch_details = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self): # CHECK IF THIS IS APPROPRIATE
        '''
        Function that will help in debugging
        '''
        return f'User {self.name}'
