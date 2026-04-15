from flask import render_template, redirect, url_for, request
from . import clerk_bp

@clerk_bp.route('/dashboard')
def dashboard():
    return render_template('shared/dashboard.html', current_page='dashboard')