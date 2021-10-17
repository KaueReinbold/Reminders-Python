from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
import json
import datetime

from src.service.reminderService import ReminderService

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

        result = ReminderService.save(
            title=title,
            description=description,
            limit_date=limit_date,
            is_done=is_done,
            user_id=current_user.id
        )

        if result.is_valid:
            flash(result.message, category='success')
        else:
            flash(result.message, category='error')

    reminders = ReminderService.get_all_by_user_id(current_user.id)

    return render_template('home.html', user=current_user, reminders=reminders)


@views.route('/delete-reminder', methods=['POST'])
def delete_reminder():
    data = json.loads(request.data)
    id = data['id']

    ReminderService.delete(current_user.id, id)

    return jsonify({})
