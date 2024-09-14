from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .. import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    question1 = db.Column(db.String(150), nullable=False)
    question1_answer = db.Column(db.String(150), nullable=False)
    question2 = db.Column(db.String(150), nullable=False)
    question2_answer = db.Column(db.String(150), nullable=False)
