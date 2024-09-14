# welcome.py ==> main
from flask import render_template

from . import main


@main.route("/")
def welcome():
    return render_template(
        "welcome.html",
        title="Welcome To Cat Store",
        custom_Css="welcome",
    )
