from flask import render_template,redirect,url_for,flash,request
from . import auth
from flask_login import login_user
from ..models.user import User
from ..models.roles import Role
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from . import views,forms

@auth.route('/login', methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            print(login_form.password.data)
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html',login_form = login_form,title = title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    roles = Role.get_roles()
    for role in roles:
        print(role.name)

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(roles_id = form.role.data.id, first_name=form.first_name.data,other_names=form.other_names.data, username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to watchlist","email/welcome",user.email,user=user)
        print(mail_message)

        return redirect(url_for('auth.login'))
    
    data = {
        "title": "JobApp - new account",
        "registration_form":form
    }

    return render_template('auth/signup.html', context=data)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
