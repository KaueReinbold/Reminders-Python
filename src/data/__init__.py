import redis

from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

redis_db = redis.Redis(
    host='localhost',
    port=6379,
    password='P@ssw0rd',
    socket_timeout=1)


def setup_data(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

    return app
