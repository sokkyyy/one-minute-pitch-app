from flask import render_template,abort
from . import main
from flask_login import login_required # For the routes that need authentication
from ..models import Pitch,User


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
