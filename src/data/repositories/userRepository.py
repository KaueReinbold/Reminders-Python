from src.data import db
from src.data.models import User


class UserRepository:
    def get(id) -> User:
        return User.query.get(int(id))

    def get_by_email(email) -> User:
        return User.query.filter_by(email=email).first()

    def save(
        email,
        first_name,
        password
    ) -> User:
        user = User(
            email=email,
            first_name=first_name,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return user
