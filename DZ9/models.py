from bson import json_util
from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE, BooleanField

connect(db="DZ8", host="mongodb://localhost:27017")


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField())
    quote = StringField()
    meta = {"collection": "quotes"}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)


class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    is_preferred_sms = BooleanField(default=False)
    is_preferred_email = BooleanField(default=False)
    is_message_sent = BooleanField(default=False)
