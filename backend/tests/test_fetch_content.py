import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.content import fetch_content
from src.models.biketype import BikeType


class TestLoadBikeTypes(unittest.TestCase):
    def test_loads_bike_types_from_all_json_assets(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            backend_dir = Path(temp_dir) / "backend"
            assets_dir = backend_dir / "assets"
            assets_dir.mkdir(parents=True)
            content_file = backend_dir / "src" / "content" / "fetch_content.py"
            content_file.parent.mkdir(parents=True)
            content_file.touch()

            for filename, bike_name in (
                ("roadbike.json", "Road Bike"),
                ("mountainbike.json", "Mountain Bike"),
            ):
                (assets_dir / filename).write_text(
                    json.dumps(
                        {
                            "bike_types": [
                                {
                                    "name": bike_name,
                                    "components": [
                                        {"name": "Wheels", "parts": ["Rim"]}
                                    ],
                                }
                            ]
                        }
                    ),
                    encoding="utf-8",
                )
            (assets_dir / "ignored.txt").touch()

            with patch.object(fetch_content, "__file__", str(content_file)):
                bike_types = fetch_content.load_bike_types()

            self.assertEqual(
                [bike.name for bike in bike_types],
                ["Mountain Bike", "Road Bike"],
            )
            self.assertTrue(all(isinstance(bike, BikeType) for bike in bike_types))
            self.assertEqual(
                bike_types[0].bikecomponents[0].bikeparts[0].name,
                "Rim",
            )

    def test_raises_when_assets_directory_is_missing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            content_file = (
                Path(temp_dir) / "backend" / "src" / "content" / "fetch_content.py"
            )
            content_file.parent.mkdir(parents=True)
            content_file.touch()

            with patch.object(fetch_content, "__file__", str(content_file)):
                with self.assertRaisesRegex(
                    FileNotFoundError, "Bike type assets directory"
                ):
                    fetch_content.load_bike_types()
