from flask import render_template, redirect, url_for, request
from . import admin_bp

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('shared/dashboard.html', current_page='dashboard')