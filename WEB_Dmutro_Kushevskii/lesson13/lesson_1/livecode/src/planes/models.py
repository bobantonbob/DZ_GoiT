import sqlalchemy
import sqlalchemy.orm as orm

import auth.models
import database

class PlaneModel(database.Base):
    __tablename__ = 'planes'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    model: orm.Mapped[str]
    image_url: orm.Mapped[str]
    fuel_tank_volume: orm.Mapped[int]
    user_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey(
        "users.id", ondelete="CASCADE"
    ), default=None)
    user: orm.Mapped[auth.models.User] = orm.relationship(
        backref="planes"
    )
