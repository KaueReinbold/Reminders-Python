from website.models import Reminder
from website import db


class ReminderRepository:
    def get_all_by_user_id(user_id) -> list[Reminder]:
        return Reminder.query.filter_by(user_id=user_id).all()

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
