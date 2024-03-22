from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20), index=True)
    last_name: Mapped[str] = mapped_column(String(20), index=True)
    email: Mapped[str] = mapped_column(String(40), index=True)
    phone_number: Mapped[str] = mapped_column(String(20), index=True)
    birthday: Mapped[str] = mapped_column(String(20), index=True)
    extra_info: Mapped[str] = mapped_column(String(250))
