from flask import render_template,request,redirect,url_for,abort
# from app.models.user import User
# from app.models.subscribe import Subscribe
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 


@main.route('/')
def home():
    '''
    Direct you to dash-board
    '''
    data = {

     'title':'Jobo-Home',
     'user':'current_user'  
    }
    return render_template('index.html', context = data)


