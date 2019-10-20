from flask import render_template,abort,redirect,url_for
from . import main
from flask_login import login_required # For the routes that need authentication
from ..models import Pitch,User
from .forms import UpdateProfile
from .. import db


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))
    
    return render_template('profile/update.html',update_form=form)

