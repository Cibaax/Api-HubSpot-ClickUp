from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

DB_HOST = "db.g97.io"
DB_PORT = 5432
DB_USER = "developer"
DB_PASS = "qS*7Pjs3v0kw"
DB_NAME = "data_analyst"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class ApiCall(Base):
    __tablename__ = "api_calls"
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    params = Column(String)
    result = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, endpoint, params, result):
        self.endpoint = endpoint
        self.params = params
        self.result = result
        self.created_at = datetime.utcnow()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_api_call(db, endpoint, params, result):
    api_call = ApiCall(endpoint=endpoint, params=json.dumps(params), result=result)
    db.add(api_call)
    db.commit()


def setup_database():
    Base.metadata.create_all(bind=engine)
