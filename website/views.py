from flask import Blueprint, render_template, request
from flask.helpers import flash
from flask_login import login_required, current_user

from .models import Note
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_text = request.form.get('note')

        if len(note_text) < 1:
            flash('Note is too short!', category='error')
        else:
            note = Note(text=note_text, user_id=current_user.id)

            db.session.add(note)
            db.session.commit()

            flash('Note added!', category='success')

    return render_template('home.html', user=current_user)
