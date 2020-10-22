import click

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy import Column, Integer, String, Float, create_engine

import settings

base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class Card(base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    qty = Column(Integer)
    price = Column(Float)


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    base.metadata.create_all(engine)
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    base.metadata.drop_all()
    click.echo("Dropped the database")


if __name__ == "__main__":
    cli()
