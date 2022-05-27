import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from os.path import abspath, dirname

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = sqlalchemy.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
