from flask import render_template, redirect, url_for, request
from . import auth_bp

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.signin'))

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return redirect(url_for('clerk.dashboard'))
    return render_template('auth/signin.html', current_page='signin')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', current_page='signup')