import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..','..', '.env')
load_dotenv(env_path)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set!")

from getpass import getpass
from sqlmodel import SQLModel, Session, create_engine

from src.models.user import User

engine = create_engine(DATABASE_URL, echo=True)


if __name__ == "__main__":
    print("Creating tables (if necessary)")
    SQLModel.metadata.create_all(engine)

    print("--------")
    print("This script will create a user and save it in the database.")

    username = input("Please enter username\n")
    pwd = getpass("Please enter password\n")

    with Session(engine) as session:
        user = User(username=username)
        user.set_password(pwd)
        session.add(user)
        session.commit()
