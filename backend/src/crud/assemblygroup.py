from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.biketype import BikeType
from src.models.assemblygroup import AssemblyGroup, AssemblyGroupInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "assembly group"

# Read an assembly group


def read_assemblygroup(id: int, session: SessionDependency) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id))

# Read all assembly groups under a bike type


def read_all_assemblygroups_by_biketype(biketype_id: int, session: SessionDependency) -> list:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id) # Get the bike type
    if not biketype: # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Return assembly groups for this bike type
    log_print("read_all", obj_type=msg_object_type, obj_id=biketype_id)
    return biketype.assemblygroups

# Create an assembly group under a bike type


def create_assemblygroup(id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    biketype = session.get(BikeType, id) # Get the bike type
    if biketype: # If bike type exists
        assemblygroup = AssemblyGroup.model_validate(input) # Create assembly group from input
        biketype.assemblygroups.append(assemblygroup) # Append assembly group to bike type
        session.commit() # Commit the changes
        session.refresh(assemblygroup) # Refresh the assembly group instance
        log_print("create", obj_type=msg_object_type)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=id)
        )

# Read an assembly group by bike type


def read_assemblygroup_by_biketype(biketype_id: int, assemblygroup_id: int, session: SessionDependency) -> AssemblyGroup:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id) # Get the bike type
    if not biketype: # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the assembly group
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id) # Get the assembly group
    if not assemblygroup: # If assembly group does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups: # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    log_print("read", obj_id=assemblygroup_id, obj_type=msg_object_type)
    return assemblygroup


# Update an assembly group by bike type


def update_assemblygroup_by_biketype(biketype_id: int, assemblygroup_id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the assembly group
    assemblygroup = session.get(
        AssemblyGroup, assemblygroup_id)  # Get the assembly group
    if not assemblygroup:  # If assembly group does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:  # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Update the assembly group
    assemblygroup.name = input.name  # Update other fields as necessary
    session.commit()  # Commit the changes
    log_print("update", obj_id=assemblygroup_id, obj_type=msg_object_type)
    return assemblygroup  # Return the updated assembly group


# Delete an assembly group by bike type

def delete_assemblygroup_by_biketype(biketype_id: int, assemblygroup_id: int, session: SessionDependency) -> None:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)  # Get the bike type
    if not biketype:  # If bike type does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then get the assembly group
    assemblygroup = session.get(
        AssemblyGroup, assemblygroup_id)  # Get the assembly group
    if not assemblygroup:  # If assembly group does not exist, raise exception
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:  # If not, raise exception
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    session.delete(assemblygroup)  # Delete the assembly group
    session.commit()  # Commit the changes
    log_print("delete", obj_id=assemblygroup_id, obj_type=msg_object_type)
