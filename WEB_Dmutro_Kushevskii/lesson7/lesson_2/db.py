import faker
import random

import datetime
import sqlalchemy

from sqlalchemy import create_engine, DateTime, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from sqlalchemy.orm import Mapped, mapped_column, relationship

engine = create_engine('sqlite:///test_db.sqlite')
DBSession = sessionmaker(bind=engine) # Abstract sessions factory

def fake_date_time():
    return faker.Faker().date_time()

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    surname: Mapped[str | None] = mapped_column(String(250))
    addresses: Mapped[list["Address"]] = relationship(
        "Address", backref="person", cascade="all,delete"
    )


class Address(Base):
    __tablename__ = 'addresses'

    id: Mapped[int] = mapped_column(primary_key=True)
    street_name: Mapped[str]
    street_number: Mapped[str | None]
    post_code: Mapped[str] = mapped_column(String(250), nullable=False)
    person_id = mapped_column(sqlalchemy.Integer, ForeignKey("persons.id", ondelete="CASCADE"))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(), default=func.now(), onupdate=fake_date_time
    )


def init_db():
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    fake_data = faker.Faker()

    persons_amount = 15

    with DBSession() as session:
        for _ in range(persons_amount):
            person = Person(name=fake_data.name())
            for _ in range(2):
                person.addresses.append(
                    Address(
                        street_name=fake_data.address(),
                        post_code=fake_data.zipcode(),
                    )
                )
            session.add(person)

        session.commit()


def show_db():
    with DBSession() as session:
        print("Persons----------------------------------")
        for person in session.query(Person).all():
            print(person.name)

        print("Addresses--------------------------------")
        for address in session.query(Address).all():
            print(f"{address.id}|{address.street_name}|{address.person.name}") # |{address.updated_at}")


def drop_db():
    with DBSession() as session:
        session.query(Person).delete()
        session.query(Address).delete()

        session.commit()

def delete_person(name: str):
    with DBSession() as session:
        user = session.query(Person).filter_by(name = name).one()
        session.delete(user)
        session.commit()

def update_db():
    with DBSession() as session:
        session.query(Address).filter_by(id = 1).update({Address.street_name: "Bob"})
        session.commit()

if __name__ == "__main__":
    init_db()
    # delete_person("Sarah Taylor")
    # show_db()
    # update_db()
    # show_db()
    # drop_db()
