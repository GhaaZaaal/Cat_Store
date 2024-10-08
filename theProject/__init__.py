# __init__.py ==> theProject
from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
db = SQLAlchemy()
DB_NAME = "database.db"

from theProject.models import Cat, User


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    csrf.init_app(app)
    db.init_app(app)

    from theProject.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from theProject.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def create_database(app):
    if not path.exists("theProject/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")
