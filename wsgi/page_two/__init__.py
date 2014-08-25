from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app as app

app_two = Blueprint('page_two', __name__, url_prefix='/page_two')


@app_two.route('/')
def index():
    return render_template('page_two/index.html')
