"""
Flask Blueprint Docs:  http://flask.pocoo.org/docs/api/#flask.Blueprint

This file is used for both the routing and logic of your
application.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from proxy import proxy_view
from . import settings

views = Blueprint('views', __name__, static_folder='../static',
                  template_folder='../templates')


@views.route('/')
def home():
    """Render website's index page."""
    return render_template('index.html')


@views.route('/api/<path:api_path>')
def api(api_path):
    """This is a simple API proxy."""
    response = proxy_view(settings.DATASET_ROOT + api_path)
    return response


# The functions below should be applicable to all Flask apps.

@views.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
