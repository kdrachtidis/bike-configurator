from dataclasses import dataclass

@dataclass
class BikeTypeMessages:
    tags: str = "Bike Type"
    description_create: str = "Create a bike type."
    description_read_all: str = "Get the list of all bike types."
    description_read: str = "Get a specific bike type based on its ID."
    description_delete: str = "Remove a specific bike type based on its ID."
    description_update: str = "Edit a specific bike type based on its ID."

@dataclass
class BikeComponentsMessages:
    tags: str = "Bike Component"
    description_create: str = "Create a bike component."
    description_read_all: str = "Get the list of all bike components."
    description_read: str = "Read a specific bike component within a bike type."
    description_delete: str = "Delete a specific bike component within a bike type."
    description_update: str = "Update a specific bike component within a bike type."

@dataclass
class BikePartsMessages:
    tags: str = "Bike Parts"
    description_create: str = "Create a new bike part within the hierarchy"
    description_read_all: str = "Get the list of all bike parts."
    description_read: str = "Get a specific bike part based on its ID."
    description_get_group_id: str = "Read a specific bike part within the hierarchy"
    description_delete: str = "Delete a specific bike part within the hierarchy."
    description_update: str = "Update a specific bike part within the hierarchy."

@dataclass
class BikeProductsMessages:
    tags: str = "Bike Products"
    description_create: str = "Add a bike product."
    description_read_all: str = "Get the list of all bike products."
    description_read: str = "Get a specific bike product based on its ID."
    description_delete: str = "Remove a specific bike product based on its ID."
    description_update: str = "Edit a specific bike product based on its ID."