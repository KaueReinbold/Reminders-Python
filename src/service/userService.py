from werkzeug.security import generate_password_hash, check_password_hash

from src.service.serviceResult import ServiceResult
from src.data.repositories.userRepository import UserRepository


class UserService:
    def save(
        email,
        first_name,
        password,
        passwordConfirmation,
    ) -> ServiceResult:
        result = None
        user = UserRepository.get_by_email(email=email)

        if user:
            result = ServiceResult(False, 'Email already taken.')
        elif len(email) < 4:
            result = ServiceResult(
                False, 'Email must be greater than 3 characters.')
        elif len(first_name) < 2:
            result = ServiceResult(
                False, 'First Name must be greater than 1 characters.')
        elif password != passwordConfirmation:
            result = ServiceResult(False, 'Passwords don\'t match.')
        elif len(password) < 7:
            result = ServiceResult(
                False, 'Password must be at least 7 characters.')
        else:
            user = UserRepository.save(
                email,
                first_name,
                generate_password_hash(password, 'sha256')
            )

            result = ServiceResult(True, 'Account created!.', user)

        return result

    def login(email, password):
        user = UserRepository.get_by_email(email=email)

        if user and check_password_hash(user.password, password):
            return ServiceResult(True, 'Logged in successfully!', user)
        else:
            return ServiceResult(False, 'Email or password not valid!')
