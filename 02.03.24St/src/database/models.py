from datetime import datetime

from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, StringField, IntField


class Users(Document):
    meta = {'collection': 'Users', "db_alias": "blended_1", 'allow_inheritance': True}
    user_id = IntField()
    first_name = StringField(null=False)
    last_name = StringField(null=True)
    username = StringField(null=True)
    language_code = StringField(null=False)
    phone_number = StringField(null=True)
    is_active = BooleanField(default=True)
    created = DateTimeField(default=datetime.now)


