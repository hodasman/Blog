from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from blog.models import User

from blog.forms.auth import UserLoginForm


auth_app = Blueprint("auth_app", __name__, url_prefix="/auth", static_folder="../static")


@auth_app.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))
    return render_template('auth/login.html', form=UserLoginForm(request.form))


@auth_app.route('/login', methods=('POST',))
def login_post():
    form = UserLoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            flash('Check your login details')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('users_app.profile', pk=user.id))

    return render_template('auth/login.html', form=form)


@auth_app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
