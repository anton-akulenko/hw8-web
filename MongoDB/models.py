from mongoengine import StringField, Document, ReferenceField, ListField, CASCADE
import connect

class Author(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    meta = {"allow_inheritance": True}

