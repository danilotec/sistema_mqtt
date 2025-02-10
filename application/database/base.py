from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.configs.configs import ConfigDatabase

Base = declarative_base()
engine = create_engine(ConfigDatabase().database_uri)
SessionLocal = sessionmaker(bind=engine)