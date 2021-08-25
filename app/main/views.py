from flask import render_template, request, redirect, url_for, abort
# from app.models.user import User
# from app.models.subscribe import Subscribe
from app import db, photos
from ..models.job import Jobs
from . import main
from flask_login import login_required, current_user
import markdown2
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


@main.route('/user-dash', methods=['GET', 'POST'])
def user_dash():
    form = NewJobForm()
    job_listings = Jobs.get_joblistings(current_user.get_id())

    data = {
        'title': 'user-dash',
        'user': current_user,
        'new_job_form': form,
        'job_listings':job_listings
    }
    
    if form.validate_on_submit():
        new_job = Jobs(commitment=form.commitment.data, department=form.department.data, team=form.team.data,
                       location=form.location.data, descriptionPlain=form.descriptionPlain.data, posted_by=current_user.get_id())

        db.session.add(new_job)
        db.session.commit()
        
        return redirect(url_for('.user_dash'))

    return render_template('index.html', context=data)


@main.route('/employer/add-job', methods=['GET', 'POST'])
@login_required
def new_job():
    '''
    View function that handles add new job request
    '''

    form = NewJobForm()

    if form.validate_on_submit():
        new_job = Jobs(job_id=form.job_id.data, commitment=form.commitment.data, department=form.department.data, team=form.team.data,
                       location=form.location.data, descriptionPlain=form.descriptionPlain.data, posted_by=current_user.get_id())

        db.session.add(new_job)
        db.session.commit()

    return redirect(url_for('.user_dash'))
