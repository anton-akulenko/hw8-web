from mongoengine import StringField, BooleanField, Document
import connect

class Contact(Document):
    fullname = StringField(max_length=50)
    email = StringField(max_length=50)
    status = BooleanField(default=False)