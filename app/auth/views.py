from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from . import auth
from ..email import mail_message

@auth.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,password=form.password.data)
        user.pic_path = f'photos/avatar.png'
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to OnePitch",'email/welcome_user',user.email,user=user)
        
        return redirect(url_for('auth.login'))
    
    title = "New Account"
    return render_template('auth/register.html',title=title, register_form=form)



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid login credentials.')
    
    title = "PitchApp login"
    return render_template('auth/login.html',title=title,login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))