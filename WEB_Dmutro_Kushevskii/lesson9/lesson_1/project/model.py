from datetime import datetime

from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    img_url: Mapped[str] = mapped_column(String(250))
    rating: Mapped[int]
    title: Mapped[str] = mapped_column(String(250), unique=True)
    price: Mapped[float]
    created: Mapped[datetime] = mapped_column(default=datetime.now())
