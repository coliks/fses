from flask import render_template, redirect, url_for, request
from . import admin_bp

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('shared/dashboard.html', current_page='dashboard')

@admin_bp.route('/establishments')
def establishments():
    return render_template('shared/establishment_management.html', current_page='establishments')


@admin_bp.route('/map')
def map():
    return render_template('shared/map.html', current_page='map')


@admin_bp.route('/users')
def users():
    return render_template('admin/user_management.html', current_page='users')