from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from credenciales import *

SQLALCHEMY_DATABASE_URL = f"postgresql://{USUARIO}:{PASSWORD}@{HOST}/{DB_NOMBRE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()