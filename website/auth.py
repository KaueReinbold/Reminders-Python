from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

from src.data.repositories.userRepository import UserRepository

auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = UserRepository.get_by_email(email=email)

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)

            flash('Logged in successfully!', category='success')

            return redirect(url_for('views.home'))
        else:
            flash('Email or password not valid!', category='error')

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

        user = UserRepository.get_by_email(email=email)

        if user:
            flash('Email already taken.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif password != passwordConfirmation:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = UserRepository.save(
                email,
                first_name,
                generate_password_hash(password, 'sha256')
            )

            login_user(new_user, remember=True)

            flash('Account created!.', category='success')

            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)
