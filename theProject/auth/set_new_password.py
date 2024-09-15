# set_new_password.py ==> auth
from flask import flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from .. import db
from ..models import User
from . import auth


@auth.route("/password_reset/confirm_mail/<int:user_id>", methods=["GET", "POST"])
def set_new_password(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not password1 or not password2:
            flash("All fields are required.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="error")
        else:
            # Update user password
            user.password = generate_password_hash(password1, method="pbkdf2:sha256")
            db.session.commit()
            flash("Your password has been updated successfully.", category="success")
            return redirect(url_for("auth.login"))

    return render_template(
        "set_new_password.html",
        title="Cat Store - Reset Password - Confirm Mail",
        custom_Css="confirm_mail",
        user=user,
    )
