from flask import render_template, request
from app import app, db, basic_auth
from app.models import *
import datetime


@app.route('/')
@app.route('/index')
def index():

    def safe_get(headlines, index):
        record = headlines[index] if index < len(headlines) else None
        try:
            return record.person, record.created_at.date(), record.url
        except:
            return None, datetime.datetime.now(), None

    try:
        headlines = Headline.objects.order_by('-created_at')
        person, created_at, url = safe_get(headlines,0)
        days_since = (datetime.datetime.now().date() - created_at).days

        return render_template('index.html',
                            days_since=str(days_since),
                            url=str(url),
                            person=str(person))

    except Exception as e:
        return str(e)

@app.route('/recv', methods = ['POST'])
@basic_auth.required
def recv():
    try:
        person = str(request.form['person'])
        url   = str(request.form['url'])
        headline = Headline(url=url, person=person)
        headline.save()
        return str(headline)
    except Exception as e:
        return str(e)
