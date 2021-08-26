from app.models.job import Jobs
from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from .forms import UpdateProfile, UpdateBio
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
 
    return render_template('landing.html', context=data)

@main.route('/user-dash')
@login_required
def user_dash():

    data = {
        'title': 'userdash',
        'user':current_user 

        
    }

    jobs = Jobs.query.all()
    single_job = Jobs.query.filter_by(id=1).first()


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


@main.route('/user-profile', methods=['GET', 'POST'])
@login_required
def user_profile():

    # user = User.query.filter_by(username = uname).first()

    # if user is None:
    #     abort(404)
    form = UpdateBio()
    if form.validate_on_submit():
        current_user.bio = form.bio.data
        db.session.add(current_user)
        db.session.commit()

        return redirect (url_for ("main.user_profile"))
        
    data = {
    'title': 'User profile',
    'user':current_user 

        
    }


    return render_template('userProfile.html', context=data, form=form)



@main.route('/user-profile/<uname>')
@login_required
def update_bio(uname):

    user = User.query.filter_by(username = uname).first()

    # if user is None:
    #     abort(404)
    form = UpdateBio()
    if form.validate_on_submit():
        current_user.bio = form.bio.data
        db.session.add(current_user)
        db.session.commit()

        return redirect (url_for ("main.user_profile"))

        
    data = {
    'title': 'User profile',
    'user':current_user 

        
    }


    return render_template('userProfile.html', context=data, form=form)

