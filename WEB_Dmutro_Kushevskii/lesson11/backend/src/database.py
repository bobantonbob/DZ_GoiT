import sqlalchemy
import sqlalchemy.orm as orm

import planes.models

BASES = [
    planes.models.Base.metadata
]

DBSession = None

def connect():
    global DBSession

    engine = sqlalchemy.create_engine('sqlite:///planes.sqlite')

    for base_meta in BASES:
        base_meta.drop_all(engine)
        base_meta.create_all(engine)
        base_meta.bind = engine

    DBSession = orm.sessionmaker(bind=engine)

def get_database():
    if DBSession is None:
        connect()

    db = DBSession()

    try:
        yield db
    finally:
        db.close()
