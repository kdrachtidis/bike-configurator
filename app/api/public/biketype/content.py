from sqlmodel import Session

from app.api.public.biketype.models import BikeType
from app.api.utils.database import engine

def create_biketypes():
    biketype_1 = BikeType(name="BMX")
    biketype_2 = BikeType(name="Rennrad")
    biketype_3 = BikeType(name="MtB")
    biketype_4 = BikeType(name="Gravel")

    session = Session(engine)

    session.add(biketype_1)
    session.add(biketype_2)
    session.add(biketype_3)
    session.add(biketype_4)

    session.commit()

    session.close()