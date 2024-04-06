import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
    pass


class PlaneModel(Base):
    __tablename__ = 'planes'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    model: orm.Mapped[str]
    image_url: orm.Mapped[str]
    fuel_tank_volume: orm.Mapped[int]
