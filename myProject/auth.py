from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import Cat, User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Logged in successfully!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("auth.homePage"))
        else:
            flash("Login failed. Check your email and password.", category="error")
    return render_template(
        "login.html",
        title="Cat Store - LogIn",
        custom_Css="login",
    )


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email").strip()
        first_name = request.form.get("firstName").strip()
        last_name = request.form.get("lastName").strip()
        phone_number = request.form.get("phoneNumber").strip()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if (
            not email
            or not first_name
            or not last_name
            or not phone_number
            or not password1
            or not password2
        ):
            flash("All fields are required.", category="error")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists.", category="error")
        elif len(phone_number) < 10:
            flash("Invalid phone number format.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
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


def get_filtered_cats(color, eye_color, age, gender):
    # Assuming you have a Cat model or cat data structure
    query = Cat.query
    if color:
        query = query.filter_by(color=color)
    if eye_color:
        query = query.filter_by(eye_color=eye_color)
    if age:
        query = query.filter_by(age=age)
    if gender:
        query = query.filter_by(gender=gender)

    return query.all()


@auth.route("/home", methods=["GET", "POST"])
@login_required
def homePage():
    if request.method == "POST":
        color = request.form.get("color")
        eye_color = request.form.get("eye_color")
        age = request.form.get("age")
        gender = request.form.get("gender")

        filtered_cats = get_filtered_cats(color, eye_color, age, gender)
        return render_template(
            "gallery.html",
            title="Cat Store",
            custom_Css="home",
            cats=filtered_cats,
        )
    return render_template(
        "home.html",
        title="Cat Store",
        custom_Css="home",
    )


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
        title="Profile",
    )


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for("auth.login"))
