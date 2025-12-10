from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart
from src.models.bikeproduct import BikeProduct


def set_roadbike():
    RoadBike = BikeType(name="Rennrad")

    def set_component_1():
        BikeComponent_1 = BikeComponent(name="Antrieb", biketypes=[RoadBike])

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

        return [BikeComponent_1, BikePart_1, BikePart_2, BikePart_3, BikePart_4, BikePart_5, BikePart_6, BikePart_7, BikePart_8, BikePart_9, BikePart_10, BikePart_11, BikePart_12, BikePart_13, BikePart_14, BikePart_15]

    def set_component_2():
        BikeComponent_2 = BikeComponent(name="Bremsen", biketypes=[RoadBike])

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
        BikePart_10 = BikePart(
            name="Innenzüge", bikecomponents=[BikeComponent_2])
        BikePart_11 = BikePart(name="Scheibenbremsbeläge",
                               bikecomponents=[BikeComponent_2])
        BikePart_12 = BikePart(name="Scheibenbremsen",
                               bikecomponents=[BikeComponent_2])

        return [BikeComponent_2, BikePart_1, BikePart_2, BikePart_3, BikePart_4, BikePart_5, BikePart_6, BikePart_7, BikePart_8, BikePart_9, BikePart_10, BikePart_11, BikePart_12]

    def set_component_3():
        BikeComponent_3 = BikeComponent(name="Laufräder", biketypes=[RoadBike])

        BikePart_1 = BikePart(name="Felgen", bikecomponents=[BikeComponent_3])
        BikePart_2 = BikePart(name="Felgenbänder",
                              bikecomponents=[BikeComponent_3])
        BikePart_3 = BikePart(
            name="Freiläufe", bikecomponents=[BikeComponent_3])
        BikePart_4 = BikePart(name="Naben", bikecomponents=[BikeComponent_3])
        BikePart_5 = BikePart(name="Schnellspanner",
                              bikecomponents=[BikeComponent_3])
        BikePart_6 = BikePart(
            name="Speichen", bikecomponents=[BikeComponent_3])
        BikePart_7 = BikePart(
            name="Nippel", bikecomponents=[BikeComponent_3])
        BikePart_8 = BikePart(
            name="Steckachsen", bikecomponents=[BikeComponent_3])
        BikePart_9 = BikePart(name="28\" Laufräder",
                              bikecomponents=[BikeComponent_3])
        BikePart_10 = BikePart(name="Tubeless Kits",
                               bikecomponents=[BikeComponent_3])
        BikePart_11 = BikePart(
            name="Kleinteile", bikecomponents=[BikeComponent_3])

        return [BikeComponent_3, BikePart_1, BikePart_2, BikePart_3, BikePart_4, BikePart_5, BikePart_6, BikePart_7, BikePart_8, BikePart_9, BikePart_10, BikePart_11]

    def set_component_4():
        BikeComponent_4 = BikeComponent(name="Bremsen", biketypes=[RoadBike])

        return [BikeComponent_4]

    def set_component_5():
        BikeComponent_5 = BikeComponent(name="Reifen", biketypes=[RoadBike])

        return [BikeComponent_5]

    def set_component_6():
        BikeComponent_6 = BikeComponent(name="Schläuche", biketypes=[RoadBike])

        return [BikeComponent_6]

    def set_component_7():
        BikeComponent_7 = BikeComponent(
            name="Komplettgruppen", biketypes=[RoadBike])
        return [BikeComponent_7]

    def set_component_8():
        BikeComponent_8 = BikeComponent(name="Laufräder", biketypes=[RoadBike])
        return [BikeComponent_8]

    def set_component_9():
        BikeComponent_9 = BikeComponent(
            name="Powermeter", biketypes=[RoadBike])
        return [BikeComponent_9]

    def set_component_10():
        BikeComponent_10 = BikeComponent(name="Sättel", biketypes=[RoadBike])
        return [BikeComponent_10]

    # Flatten all lists into one
    result = [RoadBike]
    result.extend(set_component_1())
    result.extend(set_component_2())
    result.extend(set_component_3())
    result.extend(set_component_4())
    result.extend(set_component_5())
    result.extend(set_component_6())
    result.extend(set_component_7())
    result.extend(set_component_8())
    result.extend(set_component_9())
    result.extend(set_component_10())
    return result
