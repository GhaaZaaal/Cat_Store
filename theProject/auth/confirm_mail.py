from flask import  request, redirect, url_for, flash, render_template
from werkzeug.security import check_password_hash
from . import auth
from ..models import User

@auth.route('/password_reset/<int:user_id>', methods=["GET", "POST"])
def confirm_mail(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == "POST":
        question1_answer = request.form.get("question1_answer").strip().lower()
        question2_answer = request.form.get("question2_answer").strip().lower()
        
        if user:
            # Verify answers to security questions
            if user.question1_answer == question1_answer and user.question2_answer == question2_answer:
                flash('Correct Answers! Set your new password...', 'success')
                return redirect(url_for('auth.set_new_password', user_id=user.id))
            else:
                flash('Incorrect answers to security questions', 'error')
                
    return render_template(
        "confirm_mail.html",
        title="Cat Store - Reset Password - Confirm Mail",
        custom_Css="confirm_mail",
        user=user
    )
