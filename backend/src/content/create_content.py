import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
env_path =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env'))
load_dotenv(env_path)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set!")

from sqlmodel import SQLModel, Session, create_engine
from src.content.roadbike import set_roadbike

engine = create_engine(DATABASE_URL, echo=True)


def create_demo_content():
    session = Session(engine)
    session_data = set_roadbike()
    session.add_all(session_data)
    session.commit()
    session.close()


if __name__ == "__main__":
    print("Creating tables (if necessary)")
    
    SQLModel.metadata.create_all(engine)

    print("--------")
    print("Creating demo content...")
    
    create_demo_content()
