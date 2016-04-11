from flask import render_template
from app import app
from app.models import *
from app import db
import datetime


@app.route('/')
@app.route('/index')
def index():
    try:
        headlines = Headline.objects.order_by('created_at')
        most_recent = headlines[0]
        days_since = (datetime.datetime.now().date() - most_recent.created_at.date()).days

        return render_template('index.html',
                            days_since=str(days_since),
                            person=str(most_recent.person))
    except Exception as e:
        return e
