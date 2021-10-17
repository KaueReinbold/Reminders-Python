import json

from flask_restful import Resource, reqparse

from src.service.reminderService import ReminderService


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


class Reminders(Resource):
    # HACK: Get token from auth
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        args = parser.parse_args()

        user_id = args['user_id']

        reminders = ReminderService.get_all_by_user_id(user_id)

        result = []

        if len(reminders) > 0:
            result = list(map(row2dict, reminders))

        return result, 200


def init(api):
    api.add_resource(Reminders, '/reminders')
