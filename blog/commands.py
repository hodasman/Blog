import click
from werkzeug.security import generate_password_hash

from blog.extensions import db

@click.command('init-db')
def init_db():
    from blog.wsgi import app

        # import models for creating tables

    db.create_all(app=app)

@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from blog.wsgi import app

    with app.app_context():
        db.session.add(
            User(username="admin", password=generate_password_hash("admin"), is_staff=True)
        )
        db.session.commit()