import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

DB_PATH = os.path.join('.', 'data.db')


engine = create_engine('sqlite:///' + DB_PATH,
                       poolclass=NullPool,
                       pool_pre_ping=True,
                       pool_recycle=300)
db_session = scoped_session(sessionmaker(bind=engine,
                                         autocommit=False,
                                         autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from app import models
    Base.metadata.create_all(bind=engine)


if '__main__' == __name__:
    init_db()
