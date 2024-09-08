#!/usr/bin/python3

from flask import Blueprint, render_template, request
from flask_login import login_required

from .models import Cat

main = Blueprint("main", __name__)


@main.route("/")
def welcome():
    return render_template(
        "welcome.html",
        title="Welcome To Cat Store",
        custom_Css="welcome",
    )


@main.route("/gallery")
@login_required
def gallery():
    color = request.args.get("color")
    eye_color = request.args.get("eye_color")
    age = request.args.get("age")
    gender = request.args.get("gender")

    # Query the database with filters
    query = Cat.query
    if color:
        query = query.filter_by(color=color)
    if eye_color:
        query = query.filter_by(eye_color=eye_color)
    if age:
        query = query.filter_by(age=age)
    if gender:
        query = query.filter_by(gender=gender)

    cats = query.all()
    return render_template(
        "gallery.html",
        title="Cat Store - Gallery",
        custom_Css="gallery",
        cats=cats,
    )


@main.route("/confirm_reservation/<int:cat_id>")
def confirm_Reservation(cat_id):
    # Query the database to get the specific cat
    cat = Cat.query.get_or_404(cat_id)

    # Render the reservation confirmation page with the cat data
    return render_template(
        "confirm.html",
        title="Cat Store - Confirm Reservation",
        custom_Css="confirm",
        cat=cat,
    )
