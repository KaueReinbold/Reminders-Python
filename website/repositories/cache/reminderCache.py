import json
from datetime import datetime
from website import redis_db
from website.models import Reminder


def object_decoder(json_object):
    limit_date = datetime.strptime(
        json_object['limit_date'], '%Y-%m-%d %H:%M:%S')
    return Reminder(
        id=json_object['id'],
        title=json_object['title'],
        description=json_object['description'],
        limit_date=limit_date,
        is_done=json_object['is_done'],
        user_id=json_object['user_id']
    )


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


class ReminderCache:
    def exists(user_id) -> bool:
        return redis_db.exists(user_id)

    def get(user_id):
        redis_result = redis_db.get(user_id)
        return json.loads(redis_result, object_hook=object_decoder)

    def set(user_id, reminders):
        if len(reminders) > 0:
            dict_reminders = list(map(row2dict, reminders))
            json_list = json.dumps(dict_reminders)
            redis_db.set(user_id, json_list)

    def delete(user_id):
        redis_db.delete(user_id)
