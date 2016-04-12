from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine
from flask.ext.basicauth import BasicAuth
from flask_flatpages import FlatPages


app = Flask(__name__)
Bootstrap(app)
basic_auth = BasicAuth(app)
db = MongoEngine(app)
pages = FlatPages(app)


app.config["MONGODB_SETTINGS"] = {'DB': "wcdt"}
app.config["SECRET_KEY"] = "forkingqueue"
app.config['BASIC_AUTH_USERNAME'] = 'johncena'
app.config['BASIC_AUTH_PASSWORD'] = 'keyboardcat'
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'

app.url_map.strict_slashes = False

from app import views
