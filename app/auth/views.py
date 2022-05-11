from flask import render_template,url_for, flash,redirect,request
from . import auth
from flask_login import login_user, logout_user ,login_required
from ..models import User
from .. import db
from ..email import mail_message
from .forms import RegForm,LoginForm


@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm(csrf_enable=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid')
    return render_template('auth/login.html', login_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm(csrf_enable=False)
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        mail_message("Welcome to Pitch Hub","email/welcome_user.txt",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', r_form = form)