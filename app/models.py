from . import db
from datetime import datetime

class User(db.Model):
    '''
    Class to instatiate user objects.
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    '''
    Class to define the pithces made in the app
    '''
    __tablename__ = 'pithes'

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
