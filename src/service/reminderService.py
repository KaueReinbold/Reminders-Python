from src.data.repositories.reminderRepository import ReminderRepository
from src.service.serviceResult import ServiceResult


class ReminderService:
    def save(
        title,
        description,
        limit_date,
        is_done,
        user_id
    ):
        result = None

        if len(title) < 1:
            result = ServiceResult(False, 'Title is too short!')
        elif len(title) > 50:
            result = ServiceResult(False, 'Title is too long!')
        elif len(description) < 1:
            result = ServiceResult(False, 'Description is too short!')
        elif len(description) > 200:
            result = ServiceResult(False, 'Description is too long!')
        elif limit_date == None:
            result = ServiceResult(
                False, "Incorrect data format, should be YYYY-MM-DD")
        else:
            ReminderRepository.save(
                title,
                description,
                limit_date,
                is_done,
                user_id
            )

            result = ServiceResult(True, 'Reminder added!')

        return result

    def get_all_by_user_id(user_id):
        reminders = ReminderRepository.get_all_by_user_id(user_id)

        return reminders

    def delete(user_id, id):
        ReminderRepository.delete(user_id, id)
