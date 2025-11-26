from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart
from src.models.bikeproduct import BikeProduct


def set_content():
    BikeType_1 = BikeType(name="BMX")
    BikeType_2 = BikeType(name="Rennrad")
    BikeType_3 = BikeType(name="MtB")
    BikeType_4 = BikeType(name="Gravel")
    BikeType_5 = BikeType(name="Cargo")
    BikeType_6 = BikeType(name="Tour")
    BikeType_7 = BikeType(name="Trekking")
    BikeType_8 = BikeType(name="Triathlon")
    BikeType_9 = BikeType(name="Downhill")

    BikeComponent_1 = BikeComponent(name="Antrieb", biketypes=[BikeType_2])
    BikeComponent_2 = BikeComponent(name="Cockpit", biketypes=[BikeType_2])
    BikeComponent_3 = BikeComponent(name="Dämpfer", biketypes=[BikeType_3])
    BikeComponent_4 = BikeComponent(name="Bremsen", biketypes=[BikeType_2])
    BikeComponent_5 = BikeComponent(name="Gabeln", biketypes=[BikeType_3])
    BikeComponent_6 = BikeComponent(name="Rahmen", biketypes=[BikeType_2])
    BikeComponent_7 = BikeComponent(name="Reifen", biketypes=[BikeType_2])
    BikeComponent_8 = BikeComponent(name="Schläuche", biketypes=[BikeType_2])
    BikeComponent_9 = BikeComponent(
        name="Komplettgruppen", biketypes=[BikeType_2])
    BikeComponent_10 = BikeComponent(name="Laufräder", biketypes=[BikeType_2])
    BikeComponent_11 = BikeComponent(name="Powermeter", biketypes=[BikeType_2])
    BikeComponent_12 = BikeComponent(name="Sättel", biketypes=[BikeType_2])
    BikeComponent_13 = BikeComponent(
        name="Sattelstützen", biketypes=[BikeType_2])
    BikeComponent_14 = BikeComponent(name="Schaltung", biketypes=[BikeType_2])

    BikePart_1 = BikePart(
        name="Adapter", bikecomponents=[BikeComponent_4])
    BikePart_2 = BikePart(
        name="Aussenhüllen", bikecomponents=[BikeComponent_4])
    BikePart_3 = BikePart(
        name="Bremsflüssigkeit", bikecomponents=[BikeComponent_4])
    BikePart_4 = BikePart(
        name="Bremsgriffe", bikecomponents=[BikeComponent_4])
    BikePart_5 = BikePart(
        name="Bremsleitungen", bikecomponents=[BikeComponent_4])
    BikePart_6 = BikePart(
        name="Bremsscheiben", bikecomponents=[BikeComponent_4])
    BikePart_7 = BikePart(
        name="Entlüftungskits", bikecomponents=[BikeComponent_4])
    BikePart_8 = BikePart(
        name="Felgenbremsbeläge", bikecomponents=[BikeComponent_4])
    BikePart_9 = BikePart(
        name="Felgenbremsen", bikecomponents=[BikeComponent_4])
    BikePart_10 = BikePart(
        name="Innenzüge", bikecomponents=[BikeComponent_4])
    BikePart_11 = BikePart(
        name="Scheibenbremsbeläge", bikecomponents=[BikeComponent_4])
    BikePart_12 = BikePart(
        name="Scheibenbremsen", bikecomponents=[BikeComponent_4])
    BikePart_13 = BikePart(
        name="Felgen", bikecomponents=[BikeComponent_10])
    BikePart_14 = BikePart(
        name="Felgenbänder", bikecomponents=[BikeComponent_10])
    BikePart_15 = BikePart(
        name="Freiläufe", bikecomponents=[BikeComponent_10])
    BikePart_16 = BikePart(
        name="Naben", bikecomponents=[BikeComponent_10])
    BikePart_17 = BikePart(
        name="Schnellspanner", bikecomponents=[BikeComponent_10])
    BikePart_18 = BikePart(
        name="Speichen", bikecomponents=[BikeComponent_10])
    BikePart_19 = BikePart(
        name="Nippel", bikecomponents=[BikeComponent_10])
    BikePart_20 = BikePart(
        name="Steckachsen", bikecomponents=[BikeComponent_10])

    BikeProduct_1 = BikeProduct(
        name="SHIMANO BREMSSCHEIBE SM-RT30 CENTER LOCK", source="bike24.de", price="8.99")
    BikeProduct_2 = BikeProduct(
        name="SHIMANO BREMSLEITUNG SM-BH90-SS KÜRZBAR FÜR XTR (M9100), DEORE, LX, MT520", source="bike-discount.de", price="13.99")
    BikeProduct_3 = BikeProduct(
        name="SPECIALIZED PATHFINDER PRO 28 FALTREIFEN", source="bike-discount.de", price="37.99")
    BikeProduct_4 = BikeProduct(
        name="PROLOGO NAGO R4 PAS 3DMSS NACK SADDLE", source="ebay.de", price="369")
    BikeProduct_5 = BikeProduct(
        name="SHIMANO SLX CS-M7000-11 11-SPEED CASSETTE", source="bike-components.de", price="39.99")
    BikeProduct_6 = BikeProduct(
        name="SHIMANO XT / XTR / SLX CN-HG95 10-SPEED CHAIN", source="bike-components.de", price="18.99")
    BikeProduct_7 = BikeProduct(
        name="BLACK INC CARBON LENKER-VORBAU-EINHEIT", source="bike-components.de", price="539")
    BikeProduct_8 = BikeProduct(
        name="FIZIK TEMPO MICROTEX BONDCUSH SOFT LENKERBAND", source="bike24.de", price="19.99")
    BikeProduct_9 = BikeProduct(
        name="SHIMANO B05S-RX BRAKE PADS", source="bike24.de", price="5.99")
    BikeProduct_10 = BikeProduct(
        name="CHROMAG DUNE LOCK-ON LENKERGRIFFE", source="bike-components.de", price="28.99")
    BikeProduct_11 = BikeProduct(
        name="Crankbrothers Stamp 1 Plattformpedal klein - schwarz", source="bike-components.de", price="19.99")
    BikeProduct_12 = BikeProduct(
        name="SHIMANO 105 KURBELGARNITUR FC-R7000 HOLLOWTECH II", source="bike-discount.de", price="100")

    return [BikeType_1, BikeType_2, BikeType_3, BikeType_4, BikeType_5, BikeType_6, BikeType_7, BikeType_8, BikeType_9, BikeComponent_1, BikeComponent_2, BikeComponent_3, BikeComponent_4, BikeComponent_5, BikeComponent_6, BikeComponent_7,
            BikeComponent_8, BikeComponent_9, BikeComponent_10, BikeComponent_11, BikeComponent_12, BikeComponent_13, BikeComponent_14, BikePart_1, BikePart_2, BikePart_3, BikePart_4, BikePart_5, BikePart_6, BikePart_7,
            BikePart_8, BikePart_9, BikePart_10, BikePart_11, BikePart_12, BikePart_13, BikePart_14, BikePart_15, BikePart_16, BikePart_17, BikePart_18, BikePart_19, BikePart_20, BikeProduct_1, BikeProduct_2, BikeProduct_3, BikeProduct_4, BikeProduct_5, BikeProduct_6, BikeProduct_7, BikeProduct_8, BikeProduct_9, BikeProduct_10, BikeProduct_11, BikeProduct_12]
