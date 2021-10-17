from website.models import Reminder


class ReminderRepository:
    def get_all_by_user_id(user_id) -> list[Reminder]:
        return Reminder.query.filter_by(user_id=user_id).all()
