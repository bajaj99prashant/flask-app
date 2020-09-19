from flask import render_template
from . import auth
from flask_login import login_required, login_user
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            
    return render_template('auth/login.html', form=form)

@auth.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'