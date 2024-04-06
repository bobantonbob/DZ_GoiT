import os
from dotenv import load_dotenv
from datetime import datetime

from mongoengine import connect
from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField


class Tag(EmbeddedDocument):
    name = StringField()


class Record(EmbeddedDocument):
    description = StringField()
    done = BooleanField(default=False)


class Notes(Document):
    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}

load_dotenv()

connect(
    db='notes', host="localhost", port=27017,
    username="root", password="example"
)

tag = Tag(name='Purchases')

record1 = Record(description='Buying sausage')
record2 = Record(description='Buying milk')
record3 = Record(description='Buying oil')

Notes(
    name='Shopping',
    records=[
        record1, record2, record3
    ],
    tags=[tag, ]
).save()

Notes(
    name='Going to the movies',
    records=[
        Record(description='Went to see the Avengers'),
    ],
    tags=[
        Tag(name='Fun'),
    ]
).save()


notes = Notes.objects()
for note in notes:
    print("-------------------")
    records = [
        f'description: {record.description}, done: {record.done}'
        for record in note.records
    ]

    tags = [tag.name for tag in note.tags]
    print(
        f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}"
    )

notes = Notes.objects(tags__name='Fun')
for note in notes:
    records = [
        f'description: {record.description}, done: {record.done}'
        for record in note.records
    ]

    tags = [tag.name for tag in note.tags]
    print(
        f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}"
    )


# _id = None
# note = Notes.objects(id=_id)
# note.update(name='New name')

# _id = None
# note = Notes.objects(id=_id).delete()

# class Org(Document):
#     owner = ReferenceField('User')

# class User(Document):
#     org = ReferenceField('Org', reverse_delete_rule=CASCADE)
