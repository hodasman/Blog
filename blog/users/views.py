from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint('users_app', __name__, static_folder='../static', url_prefix='/users')

USERS = {
    1: 'Bob',
    2: 'Glen',
    3: 'John'
}

@users_app.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)

@users_app.route('/<pk>')
def get_user(pk: int):
    try:
        user_name = USERS[int(pk)]
    except KeyError:
        raise NotFound(f'User {pk} not found')
    return render_template('users/detail.html', user=user_name)



