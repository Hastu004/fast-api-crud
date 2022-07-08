import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv
load_dotenv()

print('##################################################################################')
print(os.environ)
print('##################################################################################')

print('##################################################################################')
print(os.environ['DATABASE_URL'])
print('##################################################################################')

DATABASE_URL = os.environ['DATABASE_URL']
engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
