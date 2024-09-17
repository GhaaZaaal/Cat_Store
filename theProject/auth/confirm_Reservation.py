# confrim_Reservation.py ==> auth
from datetime import datetime, timedelta

from flask import flash, redirect, render_template, request, url_for
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
            cat.reservation_time = datetime.now()
            db.session.commit()

            flash(
                f"Thank you for your reservation! { cat.name } is now waiting for you at our store for '3 Days'. You can visit us at Alexandria, Egypt. We are open from [10:00 AM To 5:00 PM]. For any inquiries, please call us at (01010101010).",
                "success",
            )
            return redirect(url_for("auth.confirm_Reservation", cat_id=cat.id))
        elif not current_user.reserved_cat and cat.reserved_by:
            flash(
                f"Sorry! { cat.name } is already reserved by another user, you can choose another one for now Or just wait for our 'NEW COLLECTION' soon!.",
                "error",
            )
            return render_template(
                "confirm_reservation.html",
                title="Cat Store - Confirm Reservation",
                cat=cat,
                gallery=True,
            )
        elif current_user.reserved_cat:
            reserved_cat = Cat.query.get_or_404(current_user.reserved_cat)
            if reserved_cat.reservation_time:
                reservation_expiration = reserved_cat.reservation_time + timedelta(
                    seconds=10
                )
                remaining_time = reservation_expiration - datetime.now()
            if not cat.reserved_by:
                cat = Cat.query.get_or_404(current_user.reserved_cat)
                flash(
                    f"You have already reserved { cat.name }",
                    "error",
                )
                return render_template(
                    "confirm_reservation.html",
                    cat=cat,
                    button_disabled=True,
                    remaining_time=remaining_time,
                )
            else:
                if current_user.reserved_cat == cat.id:
                    current_user.reserved_cat = None
                    cat.reserved_by = None
                    cat.reservation_time = None
                    db.session.commit()
                    flash(
                        f"Your Reservation for { cat.name } had been canceled!",
                        "error",
                    )
                    print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
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
                    if remaining_time.total_seconds() > 0:
                        send_time = remaining_time
                    else:
                        send_time = 0

                    return render_template(
                        "confirm_reservation.html",
                        title="Cat Store - Confirm Reservation",
                        cat=cat,
                        button_disabled=True,
                        remaining_time=send_time,
                        gallery=False,
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
    elif current_user.reserved_cat:
        reserved_cat = Cat.query.get_or_404(current_user.reserved_cat)
        if reserved_cat.reservation_time:
            reservation_expiration = reserved_cat.reservation_time + timedelta(
                seconds=10
            )
            remaining_time = reservation_expiration - datetime.now()
            if cat.reserved_by:
                if current_user.reserved_cat == cat.id:
                    if remaining_time.total_seconds() > 0:
                        return render_template(
                            "confirm_reservation.html",
                            cat=cat,
                            button_disabled=True,
                            remaining_time=remaining_time,
                            gallery=False,
                        )
                    else:
                        current_user.reserved_cat = None
                        cat.reserved_by = None
                        cat.reservation_time = None
                        db.session.commit()
                        flash(
                            f"Your Reservation for { cat.name } had been Expired!",
                            "error",
                        )
                        return render_template(
                            "confirm_reservation.html",
                            title="Cat Store - Confirm Reservation",
                            cat=cat,
                            button_disabled=False,
                            reserve_again=True,
                        )
                else:
                    return render_template(
                        "confirm_reservation.html",
                        title="Cat Store - Confirm Reservation",
                        cat=cat,
                        button_disabled=False,
                        gallery=True,
                    )
            else:
                return render_template(
                    "confirm_reservation.html",
                    title="Cat Store - Confirm Reservation",
                    cat=cat,
                    button_disabled=False,
                )
