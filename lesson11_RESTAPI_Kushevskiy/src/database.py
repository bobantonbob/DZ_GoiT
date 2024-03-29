import sqlalchemy
import sqlalchemy.orm as orm

import contacts.models

CONTACT_API_MODELS = [
    contacts.models.Base.metadata,
]

DBSession = None


def connect():
    global DBSession
    engine = sqlalchemy.create_engine("sqlite:///contacts.sqlite")

    for base_metadata in CONTACT_API_MODELS:
        base_metadata.drop_all(engine)
        base_metadata.create_all(engine)
        base_metadata.bind = engine

    DBSession = orm.sessionmaker(bind=engine)


def get_database():
    if DBSession is None:
        connect()
    db = DBSession()

    try:
        yield db
    finally:
        db.close()
