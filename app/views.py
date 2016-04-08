from flask import render_template
from app import app
from app.models import *
import datetime
from babel.dates import format_datetime

@app.route('/')
@app.route('/index')
def index():
    headlines = Headline.objects.order_by('created_at')
    most_recent = headlines[0]
    days_since = (datetime.datetime.now().date() - most_recent.created_at.date()).days
    return render_template('index.html',
                        days_since=str(days_since),
                        headlines=headlines)



@app.template_filter('datetime')
def my_custom_format(value, format='MMMM d yyyy'):
    try:
        return format_datetime(value, format)
    except:
        return format_datetime(value)

@app.route("/test")
def test():
    return "<h1 style='color:blue'>Hello There!</h1>"
