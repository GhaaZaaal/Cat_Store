from flask import redirect, render_template, request, url_for
from flask_login import login_required

from . import auth



@auth.route("/home", methods=["GET", "POST"])
@login_required
def homePage():
    if request.method == "POST":
        color = request.form.get("color").capitalize().strip()
        eye_color = request.form.get("eye_color").capitalize().strip()
        age = request.form.get("age").lower().strip()
        gender = request.form.get("gender").capitalize().strip()

        return redirect(
            url_for(
                "auth.gallery", color=color, eye_color=eye_color, age=age, gender=gender
            )
        )

    return render_template(
        "home.html",
        title="Cat Store - Home",
        custom_Css="home",
    )
