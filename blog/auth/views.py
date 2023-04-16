from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

auth_app = Blueprint("auth_app", __name__, url_prefix="/auth", static_folder="../static")


@auth_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template(
            "auth/login.html"
        )
    from ..models import User

    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash("Check your login details")
        return redirect(url_for(".login"))
    login_user(user)
    return redirect(url_for("users_app.profile", pk=user.id))


@auth_app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))