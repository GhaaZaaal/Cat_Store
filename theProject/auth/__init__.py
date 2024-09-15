# __init__.py ==> auth
from flask import Blueprint

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Import the routes from other files in the auth folder
from . import login, register, password_reset, homePage, profile, gallery, confirm_Reservation, password_reset, confirm_mail, set_new_password
