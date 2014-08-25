from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app as app

app_one = Blueprint('page_one', __name__, url_prefix='/page_one')


@app_one.route('/')
def index():
    return render_template('page_one/index.html')
