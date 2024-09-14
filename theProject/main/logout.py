from flask import flash, redirect, url_for
from flask_login import login_required, logout_user

from . import main

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for("auth.login"))
