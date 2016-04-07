from flask import render_template
from app import app
from app.models import *
from babel.dates import format_datetime

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
        return str(e)


@app.template_filter('datetime')
def my_custom_format(value, format='MMMM d yyyy'):
    return format_datetime(value, format)

@app.route("/test")
def test():
    return "<h1 style='color:blue'>Hello There!</h1>"
