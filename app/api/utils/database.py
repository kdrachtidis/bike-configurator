from sqlmodel import SQLModel, create_engine, Session

sqlite_url = f"sqlite:///bike_configurator.db"

engine = create_engine(sqlite_url, connect_args={
                       "check_same_thread": False}, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
