
import sqlalchemy.orm as orm

from sqlalchemy import String

class Base(orm.DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column(String(20), index=True)
    last_name: orm.Mapped[str] = orm.mapped_column(String(20), index=True)
    email: orm.Mapped[str] = orm.mapped_column(String(40), index=True)
    phone_number: orm.Mapped[str] = orm.mapped_column(String(20), index=True)
    birthday: orm.Mapped[str] = orm.mapped_column(String(20), index=True)
    extra_info: orm.Mapped[str] = orm.mapped_column(String(250))
    completed: orm.Mapped[bool] = orm.mapped_column(default=False)


