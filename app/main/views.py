from flask import render_template,abort,redirect,url_for,request
from . import main
from flask_login import login_required,current_user # For the routes that need authentication
from ..models import Pitch,User,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos


@main.route('/')
def index():
    pitches = Pitch.query.all()
    title = "Home - One Minute Pitch"

    return render_template('home.html',title=title,pitches=pitches)


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

@main.route('/user/<uname>/update/pic', methods=['GET','POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/new/',methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch_details = form.details.data
        upvote = 0
        downvote = 0

        #Pitch Instance
        new_pitch = Pitch(pitch_category=category,pitch_details=pitch_details,upvote=upvote,downvote=downvote,user=current_user)

        #Save pitch
        new_pitch.save_pitch()

        return redirect(url_for('.index'))
    
    title = "New Pitch"
    return render_template('new_pitch.html',title=title, pitch_form=form)

@main.route('/comments/<int:pitch_id>',methods=['GET','POST'])
@login_required
def comments(pitch_id):
    #comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    pitch= Pitch.query.filter_by(id=pitch_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(pitch_comment=form.comment.data, pitch=pitch)
        new_comment.save_comment()

    title = "Comments"
    return render_template("comments.html",title=title,comment_form=form)