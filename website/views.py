from flask import Blueprint, render_template #Writing standard routes
from flask_login import login_required, current_user

views = Blueprint('views', __name__) #URLs are defined here #Blueprint is defined

@views.route('/') #we can type in slash to navigate the website
@login_required
def home():
    return render_template("home.html", user=current_user)



