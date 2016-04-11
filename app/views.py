from flask import render_template
from app import app
from app.models import *
from app import db
import datetime
from dateutil.parser import parse


@app.route('/')
@app.route('/index')
def index():
    try:
        headlines = Headline.objects.order_by('created_at')
        most_recent = headlines[0]
        days_since = (datetime.datetime.now().date() - most_recent.created_at.date()).days
        return render_template('index.html',
                            days_since=str(days_since),
                            headlines=headlines)
    except Exception as e:
        return e

"""
@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = parse(date)
    native = date.replace(tzinfo=None)
    format='%b %d, %Y'
    return native.strftime(format)
"""

@app.route("/test")
def test():
    #return "<h1 style='color:blue'>Hello Butts!</h1>"
    #return str(Headline.objects.order_by('created_at'))
    try:
        return str(Headline.objects)
    except Exception as e:
        return e
