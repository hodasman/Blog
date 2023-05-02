import click
from werkzeug.security import generate_password_hash

from blog.extensions import db

@click.command('init-db')
def init_db():
    from wsgi import app

        # import models for creating tables

    db.create_all(app=app)

@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username="admin", password=generate_password_hash("admin"), is_staff=True)
        )
        db.session.commit()


@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('India', 'Nepal', 'Georgia', 'Armenia', 'Poland', 'Hiking', 'Road trip')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')