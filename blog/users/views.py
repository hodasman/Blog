from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, login_user, current_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extension import db
from blog.forms.user import UserRegisterForm
from blog.models import User

users_app = Blueprint('users_app', __name__, static_folder='../static', url_prefix='/users')


@users_app.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users_app.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('users/register.html', form=form)

        _user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
            username=form.username.data
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
        errors=errors,
    )

@users_app.route('/')
@login_required
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@users_app.route('/<pk>')
@login_required
def profile(pk: int):
    user_name = User.query.filter_by(id=pk).one_or_none()
    if not user_name:
        raise NotFound(f'User {pk} not found')
    return render_template('users/detail.html', user=user_name)




