from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "wcdt"}
app.config["SECRET_KEY"] = "forkingqueue"

db = MongoEngine(app)

from app import views
