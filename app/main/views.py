from flask import render_template,request,redirect,url_for,abort
# from app.models.user import User
# from app.models.subscribe import Subscribe
from  app.models.job import Jobs
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 
from app.request import general_two


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
        'title': 'user-dash',
        'user':'current_user' 
    }
    return render_template('index.html',context=data)

@main.route('/jobs')
def jobs():
    '''
    get general jobs
    '''
    data = {

        'title':'JoboApp - Jobs'

    }
    jobs = Jobs.query.all()

    # job_one = general_two()

    one_job = None

    return render_template('general.html',context = data, one_job = one_job, jobs = jobs)

@main.route('/job-details/<int:id>')
def details(id):
    '''
    display job details
    '''

    one_job = Jobs.query.filter_by(id = id).first()

    jobs = Jobs.query.all()
    
    data = {

        'title':'detail'
    }
    return render_template('general.html',one_job=one_job, jobs = jobs, context=data)

@main.route('/jobs-category/<string:department>')
def department(department):
    '''
    
    '''
    one_job = None
    job_category = Jobs.query.filter_by(department = department).all()

    return render_template('category.html', job_cat =job_category, one_job=one_job)

@main.route('/job-cat-details/<string:department>/<int:id>')
def department_details(department,id):
    '''
    display job details
    '''
    job_category = Jobs.query.filter_by(department = department).all()

    one_job = Jobs.query.filter_by(id = id).first()
    
    data = {

        'title':'detail'
    }
    return render_template('category.html',one_job=one_job,job_cat =job_category, context=data)