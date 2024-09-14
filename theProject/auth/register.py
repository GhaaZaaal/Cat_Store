from flask import flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from .. import db
from ..models import User
from . import auth


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email").strip()
        first_name = request.form.get("firstName").strip()
        last_name = request.form.get("lastName").strip()
        phone_number = request.form.get("phoneNumber").strip()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        question1 = request.form.get("question1")
        question1_answer = request.form.get("question1_answer").strip().lower()
        question2 = request.form.get("question2")
        question2_answer = request.form.get("question2_answer").strip().lower()

        if (
            not email
            or not first_name
            or not last_name
            or not phone_number
            or not password1
            or not password2
            or not question1
            or not question1_answer
            or not question2
            or not question2_answer
        ):
            flash("All fields are required.", category="error")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists.", category="error")
        elif len(first_name) < 3:
            flash("Name must be at least 3 characters.", category="error")
        elif len(last_name) < 3:
            flash("Name must be at least 3 characters.", category="error")
        elif len(phone_number) < 10:
            flash("Invalid phone number format.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="error")
        elif len(question1_answer) < 3:
            flash("Answer must be at least 3 characters.", category="error")
        elif len(question2_answer) < 3:
            flash("Answer must be at least 3 characters.", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
                question1=question1,
                question1_answer=question1_answer,
                question2=question2,
                question2_answer=question2_answer,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for("auth.login"))

    return render_template(
        "register.html",
        title="Cat Store - Registration",
        custom_Css="register",
    )
