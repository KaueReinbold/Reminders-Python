import redis

from flask import Flask
from flask_login import LoginManager
from os import path


def create_app():
    app = Flask(__name__)

    # HACK: Add the key into a .env file
    app.config['SECRET_KEY'] = '64c1d708-3537-428f-9807-d57df3704215'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from src.data.models import User, Reminder

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
