from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine
from flask.ext.basicauth import BasicAuth


app = Flask(__name__)
Bootstrap(app)
basic_auth = BasicAuth(app)
db = MongoEngine(app)


app.config["MONGODB_SETTINGS"] = {'DB': "wcdt"}
app.config["SECRET_KEY"] = "forkingqueue"
app.config['BASIC_AUTH_USERNAME'] = 'johncena'
app.config['BASIC_AUTH_PASSWORD'] = 'keyboardcat'


from app import views
