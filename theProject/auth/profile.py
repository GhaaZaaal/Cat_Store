from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from .. import db
from . import auth

@auth.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        email = request.form.get("email").strip()
        first_name = request.form.get("firstName").strip()
        last_name = request.form.get("lastName").strip()
        phone_number = request.form.get("phoneNumber").strip()

        if not email or not first_name or not last_name or not phone_number:
            flash("All fields are required.", category="error")
        elif len(phone_number) < 10:
            flash("Invalid phone number format.", category="error")
        else:
            current_user.email = email
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.phone_number = phone_number
            db.session.commit()
            flash("Profile updated successfully!", category="success")
            return redirect(url_for("auth.profile"))

    return render_template(
        "profile.html",
        title="Cat Store - Profile",
        custom_Css="profile",
    )
