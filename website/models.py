from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    limit_date = db.Column(db.DateTime(timezone=True))
    is_done = db.Column(db.Boolean, unique=False, default=False)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    reminders = db.relationship('Reminder')
