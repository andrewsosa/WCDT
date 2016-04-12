from __future__ import print_function # In python 2.7

from flask import render_template, request
from flask_nav import Nav
from flask_nav.elements import *

from app import app, db, basic_auth, pages
from app.models import *

import datetime, sys


#
#   Navbar
#

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Celebrity Death Clock',
        View('Home', 'index'),
        View('About', 'page', path="about")
    )

nav.init_app(app)


#
#   App Routes
#

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

#@app.route('/about', strict_slashes=False)
@app.route('/<path:path>/')
def page(path):
    print("HELLO\t" + path, file=sys.stderr)
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
