from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
import json
import datetime

from .repositories.reminderRepository import ReminderRepository
from .models import Reminder
from . import db

views = Blueprint('views', __name__)


def validate_date(date_text) -> datetime:
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return None


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        limit_date = validate_date(request.form.get('limit_date'))
        is_done = bool(request.form.get('is_done'))

        if len(title) < 1:
            flash('Title is too short!', category='error')
        elif len(title) > 50:
            flash('Title is too long!', category='error')
        elif len(description) < 1:
            flash('Description is too short!', category='error')
        elif len(description) > 200:
            flash('Description is too long!', category='error')
        elif limit_date == None:
            flash("Incorrect data format, should be YYYY-MM-DD", category='error')
        else:
            reminder = Reminder(
                title=title,
                description=description,
                limit_date=limit_date,
                is_done=is_done,
                user_id=current_user.id
            )

            db.session.add(reminder)
            db.session.commit()

            flash('Reminder added!', category='success')

    reminders = ReminderRepository.get_all_by_user_id(current_user.id)

    print(type(reminders))

    return render_template('home.html', user=current_user, reminders=reminders)


@views.route('/delete-reminder', methods=['POST'])
def delete_reminder():
    data = json.loads(request.data)
    id = data['id']
    reminder = Reminder.query.get(id)

    if reminder:
        if reminder.user_id == current_user.id:
            db.session.delete(reminder)
            db.session.commit()

    return jsonify({})
