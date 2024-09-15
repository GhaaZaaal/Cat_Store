from flask_login import UserMixin

from .. import db


class Cat(db.Model):
    __tablename__ = "cats"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    eye_color = db.Column(db.String(20), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    reserved = db.Column(db.Boolean, default=False)
    reserved_by = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Cat {self.name}>"
