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
    # Retrieve filter criteria from the request
    color = request.args.get('color')
    eye_color = request.args.get('eye_color')
    age = request.args.get('age')
    gender = request.args.get('gender')

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
    return render_template('gallery.html', cats=cats)
    return render_template(
        "gallery.html",
        title="Cat Store - Gallery",
        custom_Css="gallery",
    )
