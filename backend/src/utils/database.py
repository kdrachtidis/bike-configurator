import os
from dotenv import load_dotenv
env_path =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', '..', '.env'))
load_dotenv(env_path)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set!")

from sqlmodel import SQLModel, create_engine, Session

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
