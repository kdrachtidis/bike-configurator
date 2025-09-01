from sqlmodel import Session

from app.models.assemblygroup import AssemblyGroup
from app.utils.database import engine


def create_AssemblyGroups():
    AssemblyGroup_1 = AssemblyGroup(name="Antrieb")
    AssemblyGroup_2 = AssemblyGroup(name="Cockpit")
    AssemblyGroup_3 = AssemblyGroup(name="Dämpfer")
    AssemblyGroup_4 = AssemblyGroup(name="Bremsen")
    AssemblyGroup_5 = AssemblyGroup(name="Gabeln")
    AssemblyGroup_6 = AssemblyGroup(name="Rahmen")
    AssemblyGroup_7 = AssemblyGroup(name="Reifen")
    AssemblyGroup_8 = AssemblyGroup(name="Schläuche")
    AssemblyGroup_9 = AssemblyGroup(name="Komplettgruppen")
    AssemblyGroup_10 = AssemblyGroup(name="Laufräder")
    AssemblyGroup_11 = AssemblyGroup(name="Powermeter")
    AssemblyGroup_12 = AssemblyGroup(name="Sättel")
    AssemblyGroup_13 = AssemblyGroup(name="Sattelstützen")
    AssemblyGroup_14 = AssemblyGroup(name="Schaltung")

    session = Session(engine)

    session.add(AssemblyGroup_1)
    session.add(AssemblyGroup_2)
    session.add(AssemblyGroup_3)
    session.add(AssemblyGroup_4)
    session.add(AssemblyGroup_5)
    session.add(AssemblyGroup_6)
    session.add(AssemblyGroup_7)
    session.add(AssemblyGroup_8)
    session.add(AssemblyGroup_9)
    session.add(AssemblyGroup_10)
    session.add(AssemblyGroup_11)
    session.add(AssemblyGroup_12)
    session.add(AssemblyGroup_13)
    session.add(AssemblyGroup_14)

    session.commit()

    session.close()
