from sqlmodel import Session

from app.models.bikecomponent import BikeComponent
from app.api.utils.database import engine


def create_BikeComponents():
    BikeComponent_1 = BikeComponent(
        name="SHIMANO BREMSSCHEIBE SM-RT30 CENTER LOCK", source="bike24.de", price="8.99")
    BikeComponent_2 = BikeComponent(
        name="SHIMANO BREMSLEITUNG SM-BH90-SS KÜRZBAR FÜR XTR (M9100), DEORE, LX, MT520", source="bike-discount.de", price="13.99")
    BikeComponent_3 = BikeComponent(
        name="SPECIALIZED PATHFINDER PRO 28 FALTREIFEN", source="bike-discount.de", price="37.99")
    BikeComponent_4 = BikeComponent(
        name="PROLOGO NAGO R4 PAS 3DMSS NACK SADDLE", source="ebay.de", price="369")
    BikeComponent_5 = BikeComponent(
        name="SHIMANO SLX CS-M7000-11 11-SPEED CASSETTE", source="bike-components.de", price="39.99")
    BikeComponent_6 = BikeComponent(
        name="SHIMANO XT / XTR / SLX CN-HG95 10-SPEED CHAIN", source="bike-components.de", price="18.99")
    BikeComponent_7 = BikeComponent(
        name="BLACK INC CARBON LENKER-VORBAU-EINHEIT", source="bike-components.de", price="539")
    BikeComponent_8 = BikeComponent(
        name="FIZIK TEMPO MICROTEX BONDCUSH SOFT LENKERBAND", source="bike24.de", price="19.99")
    BikeComponent_9 = BikeComponent(
        name="SHIMANO B05S-RX BRAKE PADS", source="bike24.de", price="5.99")
    BikeComponent_10 = BikeComponent(
        name="CHROMAG DUNE LOCK-ON LENKERGRIFFE", source="bike-components.de", price="28.99")
    BikeComponent_11 = BikeComponent(
        name="Crankbrothers Stamp 1 Plattformpedal klein - schwarz", source="bike-components.de", price="19.99")
    BikeComponent_12 = BikeComponent(
        name="SHIMANO 105 KURBELGARNITUR FC-R7000 HOLLOWTECH II", source="bike-discount.de", price="100")

    session = Session(engine)

    session.add(BikeComponent_1)
    session.add(BikeComponent_2)
    session.add(BikeComponent_3)
    session.add(BikeComponent_4)
    session.add(BikeComponent_5)
    session.add(BikeComponent_6)
    session.add(BikeComponent_7)
    session.add(BikeComponent_8)
    session.add(BikeComponent_9)
    session.add(BikeComponent_10)
    session.add(BikeComponent_11)
    session.add(BikeComponent_12)

    session.commit()

    session.close()
