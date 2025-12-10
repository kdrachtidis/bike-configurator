from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart
from src.models.bikeproduct import BikeProduct



def set_mountainbike():
    MountainBike = BikeType(name="Mountain Bike")

    BikeComponent_1 = BikeComponent(name="Antrieb", biketypes=[MountainBike])
    BikeComponent_2 = BikeComponent(name="Cockpit", biketypes=[MountainBike])
    BikeComponent_3 = BikeComponent(name="Rahmen", biketypes=[MountainBike])
    BikeComponent_4 = BikeComponent(name="Bremsen", biketypes=[MountainBike])
    BikeComponent_5 = BikeComponent(name="Reifen", biketypes=[MountainBike])
    BikeComponent_6 = BikeComponent(name="Schläuche", biketypes=[MountainBike])

    return [MountainBike, BikeComponent_1, BikeComponent_2, BikeComponent_3, BikeComponent_4, BikeComponent_5, BikeComponent_6]

# def set_all():

    #     BikeType_3 = BikeType(name="MtB")
    #     BikeType_4 = BikeType(name="Gravel")
    #     BikeType_5 = BikeType(name="Cargo")
    #     BikeType_6 = BikeType(name="Tour")
    #     BikeType_7 = BikeType(name="Trekking")
    #     BikeType_8 = BikeType(name="Triathlon")
    #     BikeType_9 = BikeType(name="Downhill")

        

    #     BikeProduct_1 = BikeProduct(
    #         name="SHIMANO BREMSSCHEIBE SM-RT30 CENTER LOCK", source="bike24.de", price="8.99")
    #     BikeProduct_2 = BikeProduct(
    #         name="SHIMANO BREMSLEITUNG SM-BH90-SS KÜRZBAR FÜR XTR (M9100), DEORE, LX, MT520", source="bike-discount.de", price="13.99")
    #     BikeProduct_3 = BikeProduct(
    #         name="SPECIALIZED PATHFINDER PRO 28 FALTREIFEN", source="bike-discount.de", price="37.99")
    #     BikeProduct_4 = BikeProduct(
    #         name="PROLOGO NAGO R4 PAS 3DMSS NACK SADDLE", source="ebay.de", price="369")
    #     BikeProduct_5 = BikeProduct(
    #         name="SHIMANO SLX CS-M7000-11 11-SPEED CASSETTE", source="bike-components.de", price="39.99")
    #     BikeProduct_6 = BikeProduct(
    #         name="SHIMANO XT / XTR / SLX CN-HG95 10-SPEED CHAIN", source="bike-components.de", price="18.99")
    #     BikeProduct_7 = BikeProduct(
    #         name="BLACK INC CARBON LENKER-VORBAU-EINHEIT", source="bike-components.de", price="539")
    #     BikeProduct_8 = BikeProduct(
    #         name="FIZIK TEMPO MICROTEX BONDCUSH SOFT LENKERBAND", source="bike24.de", price="19.99")
    #     BikeProduct_9 = BikeProduct(
    #         name="SHIMANO B05S-RX BRAKE PADS", source="bike24.de", price="5.99")
    #     BikeProduct_10 = BikeProduct(
    #         name="CHROMAG DUNE LOCK-ON LENKERGRIFFE", source="bike-components.de", price="28.99")
    #     BikeProduct_11 = BikeProduct(
    #         name="Crankbrothers Stamp 1 Plattformpedal klein - schwarz", source="bike-components.de", price="19.99")
    #     BikeProduct_12 = BikeProduct(
    #         name="SHIMANO 105 KURBELGARNITUR FC-R7000 HOLLOWTECH II", source="bike-discount.de", price="100")


def set_content():
    mountainbike_data = set_mountainbike()
    return mountainbike_data
