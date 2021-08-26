from flask import render_template,request,redirect,url_for,abort
from app.models.user import User
from app.models.subscribe import Subscribe
from app.models.job import Jobs
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 
from app.request import general
from .forms import NewJobForm,UpdateBio
from sqlalchemy import func,desc,asc


@main.route('/')
def home():
    '''
    Direct you to dash-board
    '''
    # total_count = Jobs.query(Jobs.id, func.count(Jobs.id)).group_by(Jobs.department).all()

    # spec_cat = Jobs.query.filter_by(department = department).all()

    # department_count = {}
    # records = Jobs.query.all()
    # for department in Jobs.query.distinct(Jobs.department):
    #     count = 0
    #     for record in records:
    #         if record.department == department.department:
    #             count +=1
    #     department_count[print(department.department)] = count        
    #     # print(department)
    #     # print(count)
    # #     department_count.append({department.department:count})
    # print(department_count.Technology)
    # for count in department_count:
    #     print(count.Technology)

    data = {
        'title': 'Jobo-Home',
        'user': current_user
    }

    return render_template('landing.html', context=data)

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

@main.route('/user-dash', methods=['GET', 'POST'])
@login_required
def user_dash():

    
    data = {
        'title': 'user-dash',
        'user': current_user,
    }
    
    if current_user.roles_id == 2:
        form = NewJobForm()

        data['new_job_form'] = form
        job_listings = Jobs.get_joblistings(current_user.get_id())
        data['job_listings'] = job_listings
    
    
        if form.validate_on_submit():
            new_job = Jobs(commitment=form.commitment.data, department=form.department.data, team=form.team.data,
                        location=form.location.data, descriptionPlain=form.descriptionPlain.data, posted_by=current_user.get_id())

            db.session.add(new_job)
            db.session.commit()
            
            return redirect(url_for('.user_dash'))
        return render_template('index.html',context=data)


    elif current_user.roles_id == 1: 
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

    user = User.query.filter_by(id = current_user.get_id()).first()

    form = UpdateBio()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.user_profile'))
    

    data = {
    'title': 'User profile',
    'user':current_user 
        
    }


    return render_template('userProfile.html', context=data, form = form)


@main.route('/jobs/', defaults={'id':0})
@main.route('/jobs/<int:id>')
def jobs(id):
    '''
    get general jobs
    '''
    print('Your in jobs')
    data = {

        'title':'JoboApp - Jobs'

    }
    if id == 0:
        one_job = Jobs.query.filter_by(id = 1).first()

    else:
        one_job = Jobs.query.filter_by(id = id).first()
    # jobs=general()
    jobs = Jobs.query.all()


    return render_template('general.html',context = data, one_job = one_job, jobs = jobs)
