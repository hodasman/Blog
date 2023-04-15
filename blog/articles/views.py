from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint('articles_app', __name__, static_folder='../static', url_prefix='/articles')

ARTICLES = {
    1: 'Git',
    2: 'Linux',
    3: 'Django'
}

@articles_app.route('/')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)

@articles_app.route('/<pk>')
def get_article(pk: int):
    try:
        art_name = ARTICLES[int(pk)]
    except KeyError:
        raise NotFound(f'Article {pk} not found')
    return render_template('articles/detail.html', article=art_name)





