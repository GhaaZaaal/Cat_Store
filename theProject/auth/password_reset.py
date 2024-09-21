# password_reset.py ==> auth
from flask import flash, redirect, render_template, request, url_for

from ..models import User
from . import auth


@auth.route("/register/password_reset", methods=["GET", "POST"])
def password_reset():
    if request.method == "POST":
        email = request.form.get("email")

        user = User.query.filter_by(email=email).first()

        if user:
            flash(
                "Your Email Exists!. Please follow these steps to procceed.", "success"
            )
            return redirect(url_for("auth.confirm_mail", user_id=user.id))
        else:
            flash("User not found", "error")

    return render_template(
        "password_reset.html",
        title="Cat Store - Reset Password",
        custom_Css="password_reset",
    )
