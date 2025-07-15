from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base


DATABASE_URL = "postgresql://postgres:Rashmeet0099@localhost:5432/Alchemy"

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return Session(engine)

    