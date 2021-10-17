from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from src.service.userService import UserService

auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        result = UserService.login(email, password)

        if result.is_valid:
            login_user(result.result, remember=True)

            flash(result.message, category='success')

            return redirect(url_for('views.home'))
        else:
            flash(result.message, category='error')

    return render_template('login.html', user=current_user)


@auth.route('logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('auth.login'))


@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('passwordConfirmation')

        result = UserService.save(
            email,
            first_name,
            password,
            passwordConfirmation
        )

        if result.is_valid:
            login_user(result.result, remember=True)

            flash(result.message, category='success')

            return redirect(url_for('views.home'))
        else:
            flash(result.message, category='error')

    return render_template('sign_up.html', user=current_user)
