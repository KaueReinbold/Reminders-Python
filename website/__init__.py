from flask import Flask


def create_app():
    app = Flask(__name__)

    # HACK: Add the key into a .env file
    app.config['SECRET_KEY'] = '64c1d708-3537-428f-9807-d57df3704215'

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
