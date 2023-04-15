from flask import Blueprint, render_template

index_app = Blueprint('index_app', __name__, static_folder='../static')

@index_app.route('/')
def main_page():
    return render_template('index.html')
