import click
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    create_engine,
    ForeignKey,
    TIMESTAMP,
)

import settings

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
Base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    records = orm.relationship("Record", back_populates="card")

    def __repr__(self):
        return f"Title: {self.title}\n"


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("card.id"))
    card = orm.relationship("Card", back_populates="records")

    qty = Column(Integer)
    price = Column(Float)
    timestamp = Column(
        "timestamp", TIMESTAMP(timezone=False), nullable=False, default=datetime.now()
    )

    def __repr__(self):
        return f"Qty: {self.qty}\nPrice: ${self.price}\nTimestamp: {self.timestamp}"


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    Base.metadata.create_all(engine)
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    Base.metadata.drop_all()
    click.echo("Dropped the database")


if __name__ == "__main__":
    cli()
