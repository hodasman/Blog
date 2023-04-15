from flask import Flask
from blog.articles.views import articles_app
from blog.index.views import index_app
from blog.users.views import users_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(index_app)
