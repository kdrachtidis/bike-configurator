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
class AssemblyGroupMessages:
    tags: str = "Assembly Group"
    description_create: str = "Create an assembly group."
    description_read_all: str = "Get the list of all assembly groups."
    description_read: str = "Read a specific assembly group within a bike type."
    description_delete: str = "Delete a specific assembly group within a bike type."
    description_update: str = "Update a specific assembly group within a bike type."

@dataclass
class AssemblyGroupModuleMessages:
    tags: str = "Assembly Group Module"
    description_create: str = "Add an assembly group module, providing the ID of the assembly group it belongs to."
    description_read_all: str = "Get the list of all assembly group modules."
    description_read: str = "Get a specific assembly group module based on its ID."
    description_get_group_id: str = "Get a specific assembly group module based on its group's and module's ID."
    description_delete: str = "Remove a specific assembly group module based on its ID."
    description_update: str = "Edit a specific assembly group module based on its ID."

@dataclass
class BikeComponentMessages:
    tags: str = "Bike Component"
    description_create: str = "Add a bike component."
    description_read_all: str = "Get the list of all bike components."
    description_read: str = "Get a specific bike component based on its ID."
    description_delete: str = "Remove a specific bike component based on its ID."
    description_update: str = "Edit a specific bike component based on its ID."