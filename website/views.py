from flask import Blueprint #Writing standard routes

views = Blueprint('views', __name__) #URLs are defined here #Blueprint is defined

@views.route('/') #we can type in slash to navigate the website
def home():
    return "<h1>Test</h1>"



