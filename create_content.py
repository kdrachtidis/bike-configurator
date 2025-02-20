import os

from sqlmodel import SQLModel, Session, create_engine

from demo.biketype import create_BikeTypes
from demo.assemblygroup import create_AssemblyGroups
from demo.assemblygroupmodule import create_AssemblyGroupModules
from demo.bikecomponent import create_BikeComponents

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def create_demo_content():
    create_BikeTypes()
    create_AssemblyGroups()
    create_AssemblyGroupModules()
    create_BikeComponents()
    yield

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    create_demo_content()
    