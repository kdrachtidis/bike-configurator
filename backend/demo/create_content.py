import os

from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set!")

from sqlmodel import SQLModel, Session, create_engine
from demo.set_content import set_content

engine = create_engine(DATABASE_URL, echo=True)


def create_demo_content():
    session = Session(engine)
    session_data = set_content()
    session.add_all(session_data)
    session.commit()
    session.close()


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    create_demo_content()
