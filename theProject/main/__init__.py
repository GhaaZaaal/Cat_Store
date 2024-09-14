from flask import Blueprint
from flask_login import login_required

main = Blueprint("main", __name__)

from . import welcome, logout
