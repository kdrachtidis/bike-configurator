import json
from pathlib import Path

from src.models.biketype import BikeType
from src.models.bikecomponent import BikeComponent
from src.models.bikepart import BikePart


def load_bike_types() -> list[BikeType]:
    assets_dir = Path(__file__).resolve().parents[2] / "assets"
    if not assets_dir.is_dir():
        raise FileNotFoundError(f"Bike type assets directory not found: {assets_dir}")

    bike_types: list[BikeType] = []

    for content_path in sorted(assets_dir.glob("*.json")):
        with content_path.open(encoding="utf-8") as file:
            data = json.load(file)

        bike_types.extend(
            BikeType(
                name=bike["name"],
                bikecomponents=[
                    BikeComponent(
                        name=component["name"],
                        bikeparts=[
                            BikePart(name=part)
                            for part in component.get("parts", [])
                        ],
                    )
                    for component in bike.get("components", [])
                ],
            )
            for bike in data["bike_types"]
        )

    return bike_types