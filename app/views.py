from flask import render_template, request
from app import app, db, basic_auth
from app.models import *
import datetime


@app.route('/')
@app.route('/index')
def index():
    try:
        headlines = Headline.objects.order_by('-created_at')
        most_recent = headlines[0]
        days_since = (datetime.datetime.now().date() - most_recent.created_at.date()).days

        return render_template('index.html',
                            days_since=str(days_since),
                            person=str(most_recent.person))
    except Exception as e:
        return e

@app.route('/recv', methods = ['POST'])
@basic_auth.required
def recv():
    try:
        person = str(request.form['person'])
        text   = str(request.form['headline'])
        headline = Headline(text=text, person=person)
        headline.save()
        return str(headline)
    except Exception as e:
        return str(e)
