from flask import render_template
from . import main
from flask_login import login_required # For the routes that need authentication



@main.route('/')
def index():
    return render_template('home.html')