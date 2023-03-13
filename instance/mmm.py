from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///recept.db', echo = True)
meta = MetaData()

students = Table(
   'recept', meta,
   Column('id', Integer, primary_key = True),
   Column('nazev', String),
   Column('text', String),
   Column('ingredience', String),
)
meta.create_all(engine)