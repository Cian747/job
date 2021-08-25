from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.subscribe import Subscribe
from app.models.job import Jobs
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 
from ..request import job_listings, job_listings2


@main.route('/')
def home():
    '''
    Direct you to dash-board
    '''
    data = {
     'title':'Jobo-Home',
     'user':'current_user'  
    }
 
    return render_template('landing.html', context=data)

@main.route('/user-dash')
def user_dash():

    data = {
        'title': 'userdash', 
        'user': 'current_user'
    }

    return render_template('index.html',context=data)

@main.route('/jobs/all')
def all_jobs():
    jobs = job_listings2()
    jobs2 = Jobs.query.all()
    data = {
        'title':'All Jobs',
        'user': current_user
    }

    return render_template('jobs.html', context = data, jobs = jobs)

