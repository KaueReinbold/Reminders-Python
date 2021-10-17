from src.data import db

from src.data.models import Reminder
from .cache.reminderCache import ReminderCache


class ReminderRepository:
    def get_all_by_user_id(user_id) -> list[Reminder]:
        reminders = []

        if ReminderCache.exists(user_id):
            reminders = ReminderCache.get(user_id)
        else:
            reminders = Reminder.query.filter_by(user_id=user_id).all()

            ReminderCache.set(user_id, reminders)

        return reminders

    def save(
        title,
        description,
        limit_date,
        is_done,
        user_id
    ) -> None:
        reminder = Reminder(
            title=title,
            description=description,
            limit_date=limit_date,
            is_done=is_done,
            user_id=user_id
        )

        db.session.add(reminder)
        db.session.commit()

        ReminderCache.delete(user_id)

    def delete(user_id, id):
        reminder = Reminder.query.filter_by(id=id, user_id=user_id).first()

        db.session.delete(reminder)
        db.session.commit()

        ReminderCache.delete(user_id)
