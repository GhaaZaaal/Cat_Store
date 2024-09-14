# confrim_Reservation.py ==> auth
from flask import flash, redirect, render_template, request, url_for

from flask_login import login_required

from ..models import User, Cat
from . import auth

@auth.route("/confirm_reservation/<int:cat_id>", methods=["GET", "POST"])
@login_required
def confirm_Reservation(cat_id):
    cat = Cat.query.get_or_404(cat_id)

    if request.method == "POST":
        flash(
            "Thank you for your reservation! The cat is now waiting for you at our store. You can visit us at Alexandria, Egypt. We are open from [10:00 AM To 5:00 PM]. For any inquiries, please call us at (01010101010).",
            "success",
        )
        return render_template(
            "confirm_reservation.html",
            title="Cat Store - Confirm Reservation",
            custom_Css="confirm",
            cat=cat,
            button_disabled=True,
        )

    return render_template(
        "confirm_reservation.html",
        title="Cat Store - Confirm Reservation",
        custom_Css="confirm",
        cat=cat,
        button_disabled=False,
    )
