from sqlmodel import Session

from app.models.assemblygroupmodule import AssemblyGroupModule
from app.utils.database import engine


def create_AssemblyGroupModules():
    AssemblyGroupModule_1 = AssemblyGroupModule(name="Brake Levers")
    AssemblyGroupModule_2 = AssemblyGroupModule(name="Aussenhüllen")
    AssemblyGroupModule_3 = AssemblyGroupModule(name="Bremsflüssigkeit")
    AssemblyGroupModule_4 = AssemblyGroupModule(name="Bremsgriffe")
    AssemblyGroupModule_5 = AssemblyGroupModule(name="Bremsleitungen")
    AssemblyGroupModule_6 = AssemblyGroupModule(name="Bremsscheiben")
    AssemblyGroupModule_7 = AssemblyGroupModule(name="Entlüftungskits")
    AssemblyGroupModule_8 = AssemblyGroupModule(name="Felgenbremsbeläge")
    AssemblyGroupModule_9 = AssemblyGroupModule(name="Felgenbremsen")
    AssemblyGroupModule_10 = AssemblyGroupModule(name="Innenzüge")
    AssemblyGroupModule_11 = AssemblyGroupModule(name="Scheibenbremsbeläge")
    AssemblyGroupModule_12 = AssemblyGroupModule(name="Scheibenbremsen")
    AssemblyGroupModule_13 = AssemblyGroupModule(name="Felgen")
    AssemblyGroupModule_14 = AssemblyGroupModule(name="Felgenbänder")
    AssemblyGroupModule_15 = AssemblyGroupModule(name="Freiläufe")
    AssemblyGroupModule_16 = AssemblyGroupModule(name="Naben")
    AssemblyGroupModule_17 = AssemblyGroupModule(name="Schnellspanner")
    AssemblyGroupModule_18 = AssemblyGroupModule(name="Speichen")
    AssemblyGroupModule_19 = AssemblyGroupModule(name="Nippel")
    AssemblyGroupModule_20 = AssemblyGroupModule(name="Steckachsen")

    session = Session(engine)

    session.add(AssemblyGroupModule_1)
    session.add(AssemblyGroupModule_2)
    session.add(AssemblyGroupModule_3)
    session.add(AssemblyGroupModule_4)
    session.add(AssemblyGroupModule_5)
    session.add(AssemblyGroupModule_6)
    session.add(AssemblyGroupModule_7)
    session.add(AssemblyGroupModule_8)
    session.add(AssemblyGroupModule_9)
    session.add(AssemblyGroupModule_10)
    session.add(AssemblyGroupModule_11)
    session.add(AssemblyGroupModule_12)
    session.add(AssemblyGroupModule_13)
    session.add(AssemblyGroupModule_14)
    session.add(AssemblyGroupModule_15)
    session.add(AssemblyGroupModule_16)
    session.add(AssemblyGroupModule_17)
    session.add(AssemblyGroupModule_18)
    session.add(AssemblyGroupModule_19)
    session.add(AssemblyGroupModule_20)

    session.commit()

    session.close()
