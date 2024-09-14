from flask import flash, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash

from flask_login import login_user

from ..models import User
from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login form submission
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Welcome back! You've successfully logged in.", "success")
            return redirect(url_for("auth.homePage"))
        else:
            flash("Oops! The email or password you entered is incorrect. Please try again.", "error")
            return render_template(
                "login.html",
                title="Cat Store - LogIn",
                custom_Css="login",
                show_register=True,
            )
    return render_template(
        "login.html",
        title="Cat Store - LogIn",
        custom_Css="login",
        show_register=False,
    )
