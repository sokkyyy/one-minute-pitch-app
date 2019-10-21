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
    bio = db.Column(db.String())
    pic_path = db.Column(db.String())
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
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches


    def __repr__(self):
        '''
        Function that will help in debugging
        '''
        return f'User {self.name}'




class Comment(db.Model):
    '''
    Class to define comments for pitches.
    '''
    __tablename__= 'comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_comment = db.Column(db.String)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))



    
    def __repr__(self): 
        '''
        Function that will help in debugging
        '''
        return f'User {self.name}'
