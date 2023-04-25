from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import Article

articles_app = Blueprint('articles_app', __name__, static_folder='../static', url_prefix='/articles')


@articles_app.route('/')
def articles_list():
    _articles = Article.query.all()
    return render_template('articles/list.html', articles=_articles)

# @articles_app.route('/<pk>')
# def get_articl(pk: int):
#     try:
#         art_name = ARTICLES[int(pk)]
#     except KeyError:
#         raise NotFound(f'Article {pk} not found')
#     return render_template('articles/detail.html', article=art_name)


@articles_app.route('/<pk>')
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).one_or_none()
    if not _article:
        raise NotFound(f'Article {pk} not found')
    return render_template('articles/detail.html', user=_article)


