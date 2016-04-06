from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
Bootstrap(app)

app.config["MONGODB_SETTINGS"] = {'DB': "wcdt"}
app.config["SECRET_KEY"] = "forkingqueue"

db = MongoEngine(app)

from app import views
