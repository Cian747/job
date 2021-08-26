from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.subscribe import Subscribe
from app.models.job import Jobs
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 
from app.request import general_two
from ..request import job_listings
from .forms import NewJobForm


@main.route('/')
def home():
    '''
    Direct you to dash-board
    '''
    data = {
        'title': 'Jobo-Home',
        'user': current_user
    }

    return render_template('landing.html', context=data)

@main.route('/user-dash')
def user_dash():

    data = {
        'title': 'userdash', 
        'user': 'current_user'
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
  
@main.route('/jobs/all')
def all_jobs():
    jobs = Jobs.query.all()
    data = {
        'title':'All Jobs',
        'user': current_user
    }

    return render_template('jobs.html', context = data, jobs = jobs)

@main.route('/user-dash')
@login_required
def user_dash():
    form = NewJobForm()
    job_listings = Jobs.get_joblistings(current_user.get_id())
   
    
    if form.validate_on_submit():
        new_job = Jobs(commitment=form.commitment.data, department=form.department.data, team=form.team.data,
                       location=form.location.data, descriptionPlain=form.descriptionPlain.data, posted_by=current_user.get_id())

        db.session.add(new_job)
        db.session.commit()
        
        return redirect(url_for('.user_dash'))

    jobs = Jobs.query.all()
    single_job = Jobs.query.filter_by(id=1).first()
    
    data = {
        'title': 'user-dash',
        'user': current_user,
        'new_job_form': form,
        'job_listings':job_listings
    }


    return render_template('index.html',context=data, jobs=jobs, single_job=single_job)


@main.route('/Job/job-details/<int:id>')
@login_required
def job_details(id):
    single_job=Jobs.query.get(id)
    jobs = Jobs.query.all()

   
    data = {
    'title': 'Job details',
    'user':current_user 

        
    }

    return render_template('index.html',single_job=single_job,jobs=jobs, context=data)


@main.route('/user-profile')
@login_required
def user_profile():

    data = {
    'title': 'User profile',
    'user':current_user 

        
    }


    return render_template('userProfile.html', context=data)


