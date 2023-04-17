from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import User

users_app = Blueprint('users_app', __name__, static_folder='../static', url_prefix='/users')


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




