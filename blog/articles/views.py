from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import ArticleAddForm
from blog.models import Article, Author, Tag

articles_app = Blueprint('articles_app', __name__, static_folder='../static', url_prefix='/articles')


@articles_app.route('/', methods=['GET'])
def articles_list():
    _articles = Article.query.all()
    return render_template('articles/list.html', articles=_articles)


@articles_app.route('/', methods=['POST'])
@login_required
def create_articles():
    form = ArticleAddForm(request.form)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        if not current_user.author:
            _author = Author(user_id=current_user.id)
            db.session.add(_author)
            db.session.commit()

        _article = Article(
            title=form.title.data,
            text=form.text.data,
            author_id=current_user.author.id
        )
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('articles_app.get_article', pk=_article.id))

    return render_template(
        'articles/create.html',
        form=form,
    )


@articles_app.route('/<pk>')
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
    if not _article:
        raise NotFound(f'Article {pk} not found')
    return render_template('articles/detail.html', article=_article)


@articles_app.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = ArticleAddForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


