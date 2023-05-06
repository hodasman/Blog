from flask import Flask
from blog import commands
from blog.extensions import db, login_manager, migrate, csrf, admin
from blog.articles.views import articles_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)
    csrf.init_app(app)
    admin.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from blog.models import User
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.index.views import index_app
    from blog.users.views import users_app
    from blog.auth.views import auth_app
    from blog.author.views import author_app
    from blog import admin

    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(index_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(author_app)

    admin.register_views()

def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_tags)
