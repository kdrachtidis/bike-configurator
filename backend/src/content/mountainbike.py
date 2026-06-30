from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart


def set_mtb():
    MountainBike = BikeType(name="Mountainbike")

    def set_component_1():
        BikeComponent_1 = BikeComponent(name="Antrieb", biketypes=[MountainBike])

        BikePart_1 = BikePart(name="Adapter-Kits",
                              bikecomponents=[BikeComponent_1])
        BikePart_2 = BikePart(name="Cleats & Schuhplatten",
                              bikecomponents=[BikeComponent_1])
        BikePart_3 = BikePart(name="Fahrradkassetten",
                              bikecomponents=[BikeComponent_1])
        BikePart_4 = BikePart(name="Fahrradketten",
                              bikecomponents=[BikeComponent_1])
        BikePart_5 = BikePart(name="Fahrradkurbeln",
                              bikecomponents=[BikeComponent_1])
        BikePart_6 = BikePart(
            name="Innenlager", bikecomponents=[BikeComponent_1])
        BikePart_7 = BikePart(name="Kettenblätter",
                              bikecomponents=[BikeComponent_1])
        BikePart_8 = BikePart(name="Kettenführungen",
                              bikecomponents=[BikeComponent_1])
        BikePart_9 = BikePart(
            name="Bashguard", bikecomponents=[BikeComponent_1])
        BikePart_10 = BikePart(
            name="Kleinteile", bikecomponents=[BikeComponent_1])
        BikePart_11 = BikePart(name="Nabenschaltung",
                               bikecomponents=[BikeComponent_1])
        BikePart_12 = BikePart(name="Pedale", bikecomponents=[BikeComponent_1])
        BikePart_13 = BikePart(name="Riemen", bikecomponents=[BikeComponent_1])
        BikePart_14 = BikePart(name="Riemenscheibe",
                               bikecomponents=[BikeComponent_1])
        BikePart_15 = BikePart(name="Verschleißsets",
                               bikecomponents=[BikeComponent_1])

        return [BikeComponent_1, BikePart_1, BikePart_2, BikePart_3, BikePart_4,
                BikePart_5, BikePart_6, BikePart_7,
                BikePart_8, BikePart_9, BikePart_10, BikePart_11, BikePart_12, BikePart_13, BikePart_14, BikePart_15]

    def set_component_2():
        BikeComponent_2 = BikeComponent(name="Bremsen", biketypes=[MountainBike])

        BikePart_1 = BikePart(name="Adapter", bikecomponents=[BikeComponent_2])
        BikePart_2 = BikePart(name="Aussenhüllen",
                              bikecomponents=[BikeComponent_2])
        BikePart_3 = BikePart(name="Bremsflüssigkeit",
                              bikecomponents=[BikeComponent_2])
        BikePart_4 = BikePart(name="Bremsgriffe",
                              bikecomponents=[BikeComponent_2])
        BikePart_5 = BikePart(name="Bremsleitungen",
                              bikecomponents=[BikeComponent_2])
        BikePart_6 = BikePart(name="Bremsscheiben",
                              bikecomponents=[BikeComponent_2])
        BikePart_7 = BikePart(name="Entlüftungskits",
                              bikecomponents=[BikeComponent_2])
        BikePart_8 = BikePart(name="Felgenbremsbeläge",
                              bikecomponents=[BikeComponent_2])
        BikePart_9 = BikePart(name="Felgenbremsen",
                              bikecomponents=[BikeComponent_2])
        BikePart_10 = BikePart(name="Felgen",
                               bikecomponents=[BikeComponent_2])
        BikePart_11 = BikePart(name="Felgenbänder",
                               bikecomponents=[BikeComponent_2])
        return [BikeComponent_2, BikePart_1, BikePart_2, BikePart_3, BikePart_4,
                BikePart_5, BikePart_6, BikePart_7,
                BikePart_8, BikePart_9, BikePart_10, BikePart_11]

    def set_component_3():
        BikeComponent_3 = BikeComponent(name="Fahrwerk", biketypes=[MountainBike])

        BikePart_1 = BikePart(name="Dämpfer",
                              bikecomponents=[BikeComponent_3])
        BikePart_2 = BikePart(name="Federgabeln",
                              bikecomponents=[BikeComponent_3])
        BikePart_3 = BikePart(name="Gabelbrücken",
                              bikecomponents=[BikeComponent_3])
        BikePart_4 = BikePart(name="Gabelschaft",
                              bikecomponents=[BikeComponent_3])
        BikePart_5 = BikePart(name="Kleinteile",
                              bikecomponents=[BikeComponent_3])
        return [BikeComponent_3, BikePart_1, BikePart_2, BikePart_3, BikePart_4, BikePart_5]
    
    def set_component_4():
        BikeComponent_4 = BikeComponent(name="Laufräder", biketypes=[MountainBike])

        BikePart_1 = BikePart(name="Felgen", bikecomponents=[BikeComponent_4])
        BikePart_2 = BikePart(name="Felgenbänder",
                              bikecomponents=[BikeComponent_4])
        BikePart_3 = BikePart(name="Naben", bikecomponents=[BikeComponent_4])
        BikePart_4 = BikePart(name="Speichen", bikecomponents=[BikeComponent_4])
        return [BikeComponent_4, BikePart_1, BikePart_2, BikePart_3, BikePart_4]
    
    result = [MountainBike]
    result.extend(set_component_1())
    result.extend(set_component_2())
    result.extend(set_component_3())
    result.extend(set_component_4())
    return result