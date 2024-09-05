from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.String(15))


class Cat(db.Model):
    __tablename__ = "cats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    eye_color = db.Column(db.String(20), nullable=False)
    age = db.Column(
        db.String(20), nullable=False
    )  # Example: 'kitten', 'adult', 'senior'
    gender = db.Column(db.String(10), nullable=False)  # 'male' or 'female'
    reserved = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(100), nullable=False)  # Path to the image file

    def __repr__(self):
        return f"<Cat {self.name}>"
