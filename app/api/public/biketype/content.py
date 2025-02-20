from sqlmodel import Session

from app.models.biketype import BikeType
from app.api.utils.database import engine


def create_BikeTypes():
    BikeType_1 = BikeType(name="BMX")
    BikeType_2 = BikeType(name="Rennrad")
    BikeType_3 = BikeType(name="MtB")
    BikeType_4 = BikeType(name="Gravel")
    BikeType_5 = BikeType(name="Cargo")
    BikeType_6 = BikeType(name="Tour")
    BikeType_7 = BikeType(name="Trekking")
    BikeType_8 = BikeType(name="Triathlon")
    BikeType_9 = BikeType(name="Downhill")

    session = Session(engine)

    session.add(BikeType_1)
    session.add(BikeType_2)
    session.add(BikeType_3)
    session.add(BikeType_4)
    session.add(BikeType_5)
    session.add(BikeType_6)
    session.add(BikeType_7)
    session.add(BikeType_8)
    session.add(BikeType_9)

    session.commit()

    session.close()
