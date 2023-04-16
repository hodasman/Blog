from flask import Flask


from .auth.views import auth_app
from .extension import db, login_manager
from blog.articles.views import articles_app
from blog.index.views import index_app
from blog.users.views import users_app
from .models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '=&kpz4*c7d98-h6uguv4n(%u-t+8jcw@witq+*ye46&7^=3zw3'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.login_view = 'auth_app.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(index_app)
    app.register_blueprint(auth_app)
