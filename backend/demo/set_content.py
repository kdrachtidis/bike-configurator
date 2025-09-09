from app.models.biketype import BikeType
from app.models.assemblygroup import AssemblyGroup
from app.models.assemblygroupmodule import AssemblyGroupModule
from app.models.bikecomponent import BikeComponent


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

    AssemblyGroup_1 = AssemblyGroup(name="Antrieb", biketypes=[BikeType_1])
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

    return [BikeType_1, BikeType_2, BikeType_3, BikeType_4, BikeType_5, BikeType_6, BikeType_7, BikeType_8, BikeType_9, AssemblyGroup_1, AssemblyGroup_2, AssemblyGroup_3, AssemblyGroup_4, AssemblyGroup_5, AssemblyGroup_6, AssemblyGroup_7,
            AssemblyGroup_8, AssemblyGroup_9, AssemblyGroup_10, AssemblyGroup_11, AssemblyGroup_12, AssemblyGroup_13, AssemblyGroup_14, AssemblyGroupModule_1, AssemblyGroupModule_2, AssemblyGroupModule_3, AssemblyGroupModule_4, AssemblyGroupModule_5, AssemblyGroupModule_6, AssemblyGroupModule_7,
            AssemblyGroupModule_8, AssemblyGroupModule_9, AssemblyGroupModule_10, AssemblyGroupModule_11, AssemblyGroupModule_12, AssemblyGroupModule_13, AssemblyGroupModule_14, AssemblyGroupModule_15, AssemblyGroupModule_16, AssemblyGroupModule_17, AssemblyGroupModule_18, AssemblyGroupModule_19, AssemblyGroupModule_20, BikeComponent_1, BikeComponent_2, BikeComponent_3, BikeComponent_4, BikeComponent_5, BikeComponent_6, BikeComponent_7, BikeComponent_8, BikeComponent_9, BikeComponent_10, BikeComponent_11, BikeComponent_12]
