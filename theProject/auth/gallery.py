# gallery.py ==> auth
from flask import render_template, request
from flask_login import login_required
from ..models import Cat
from flask_sqlalchemy import pagination

from . import auth


@auth.route("/gallery", methods=["GET", "POST"])
@login_required
def gallery():
    color = request.args.get("color")
    eye_color = request.args.get("eye_color")
    age = request.args.get("age")
    gender = request.args.get("gender")
    page = request.args.get("page", 1, type=int)
    per_page = 9  # Number of items per page

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

    cats_pagination = query.paginate(page=page, per_page=per_page, error_out=True)

    return render_template(
        "gallery.html",
        title="Cat Store - Gallery",
        custom_Css="gallery",
        cats=cats_pagination.items,
        pagination=cats_pagination,
    )
