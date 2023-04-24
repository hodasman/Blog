from flask import Flask


from blog.auth.views import auth_app
from blog.extension import db, login_manager, migrate, csrf

from blog.articles.views import articles_app
from blog.index.views import index_app
from blog.users.views import users_app



def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    db.init_app(app)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):

    migrate.init_app(app, db, compare_type=True)
    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)
    csrf.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(index_app)
    app.register_blueprint(auth_app)
