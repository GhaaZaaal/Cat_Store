# confrim_Reservation.py ==> auth
from flask import flash, render_template, request
from flask_login import current_user, login_required

from .. import db
from ..models import Cat
from . import auth


@auth.route("/confirm_reservation/<int:cat_id>", methods=["GET", "POST"])
@login_required
def confirm_Reservation(cat_id):
    cat = Cat.query.get_or_404(cat_id)

    if request.method == "POST":
        if not current_user.reserved_cat and not cat.reserved_by:
            current_user.reserved_cat = cat.id
            cat.reserved_by = current_user.id
            flash(
                f"Thank you for your reservation!\n\n\n\n\n\n{ cat.name } is now waiting for you at our store.\nYou can visit us at Alexandria, Egypt.\nWe are open from [10:00 AM To 5:00 PM].\nFor any inquiries, please call us at (01010101010).",
                "success",
            )
            db.session.commit()
            return render_template(
                "confirm_reservation.html",
                title="Cat Store - Confirm Reservation",
                cat=cat,
                button_disabled=True,
                gallery=False,
            )
        elif not current_user.reserved_cat and cat.reserved_by:
            flash(
                f"Sorry! { cat.name } is already reserved by another user, you can choose another one for now\nOr just wait for our 'NEW COLLECTION' soon!.",
                "error",
            )
            return render_template(
                "confirm_reservation.html",
                title="Cat Store - Confirm Reservation",
                cat=cat,
                gallery=True,
            )
        elif current_user.reserved_cat:
            if not cat.reserved_by:
                cat = Cat.query.get_or_404(current_user.reserved_cat)
                flash(
                    f"You have already reserved { cat.name }",
                    "error",
                )
                return render_template(
                    "confirm_reservation.html",
                    title="Cat Store - Confirm Reservation",
                    cat=cat,
                    button_disabled=True,
                )
            else:
                if current_user.reserved_cat == cat.id:
                    current_user.reserved_cat = None
                    cat.reserved_by = None
                    db.session.commit()
                    flash(
                        f"Your Reservation for { cat.name } had been canceled!",
                        "error",
                    )
                    return render_template(
                        "confirm_reservation.html",
                        title="Cat Store - Confirm Reservation",
                        cat=cat,
                        button_disabled=False,
                        gallery=True,
                    )
                else:
                    flash(
                        f"You have already reserved { cat.name }",
                        "error",
                    )
                    return render_template(
                        "confirm_reservation.html",
                        title="Cat Store - Confirm Reservation",
                        cat=cat,
                        button_disabled=True,
                    )

    if not current_user.reserved_cat and not cat.reserved_by:
        return render_template(
            "confirm_reservation.html",
            title="Cat Store - Confirm Reservation",
            cat=cat,
            button_disabled=False,
        )
    elif not current_user.reserved_cat and cat.reserved_by:
        return render_template(
            "confirm_reservation.html",
            title="Cat Store - Confirm Reservation",
            cat=cat,
            button_disabled=False,
            gallery=True,
        )
    elif current_user.reserved_cat and not cat.reserved_by:
        return render_template(
            "confirm_reservation.html",
            title="Cat Store - Confirm Reservation",
            cat=cat,
            button_disabled=False,
        )
    elif current_user.reserved_cat and cat.reserved_by:
        if current_user.reserved_cat == cat.id:
            return render_template(
                "confirm_reservation.html",
                title="Cat Store - Confirm Reservation",
                cat=cat,
                button_disabled=True,
            )
        else:
            return render_template(
                "confirm_reservation.html",
                title="Cat Store - Confirm Reservation",
                cat=cat,
                button_disabled=False,
            )
