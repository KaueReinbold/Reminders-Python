import redis

from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

redis_db = redis.Redis(
    host='localhost',
    port=6379,
    password='P@ssw0rd',
    socket_timeout=1)


def setup_data(app, database_path):

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

    db.init_app(app)

    if not path.exists(database_path):
        db.create_all(app=app)
        print('Created Database!')

    return app
