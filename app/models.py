import datetime
from flask import url_for
from app import db

class Headline(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    person = db.StringField(max_length=255, required=True, unique=True)
    url = db.StringField(max_length=255, default="#")


    def __unicode__(self):
        return self.person

    meta = {
        'ordering': ['-created_at']
    }
