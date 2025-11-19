from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.utils.logging import log_print, log_exception
from src.models.biketype import BikeType
from src.models.assemblygroup import AssemblyGroup
from src.models.assemblygroupmodule import AssemblyGroupModule, AssemblyGroupModuleInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "assembly group module"

# Read an assembly group module


def read_assemblygroupmodule(id: int, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=id))
    

# Read assembly group modules by hierarchy


def read_assemblygroupmodules_by_hierarchy(biketype_id: int, assemblygroup_id: int, session: SessionDependency) -> list:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if assembly group exists
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if not assemblygroup:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Return assembly group modules for this assembly group
    log_print("read_by_hierarchy", group_id=assemblygroup_id,
              obj_type=msg_object_type)
    return assemblygroup.assemblygroupmodules


# Create an assembly group module by hierarchy


def create_assemblygroupmodule_by_hierarchy(biketype_id: int, assemblygroup_id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if assembly group exists
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if not assemblygroup:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Create the assembly group module
    assemblygroupmodule = AssemblyGroupModule.model_validate(input)
    assemblygroup.assemblygroupmodules.append(assemblygroupmodule)
    session.commit()
    session.refresh(assemblygroupmodule)
    log_print("create", obj_type=msg_object_type)
    return assemblygroupmodule



# Read an assembly group module by hierarchy


def read_assemblygroupmodule_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, session: SessionDependency) -> AssemblyGroupModule:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if assembly group exists
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if not assemblygroup:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Then get the assembly group module
    assemblygroupmodule = session.get(AssemblyGroupModule, module_id)
    if not assemblygroupmodule:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=module_id)
        )

    # Verify that the module belongs to the specified assembly group
    if assemblygroupmodule not in assemblygroup.assemblygroupmodules:
        raise HTTPException(
            status_code=404, detail=f"Assembly group module {module_id} not found in assembly group {assemblygroup_id}"
        )

    log_print("read", obj_id=module_id, obj_type=msg_object_type)
    return assemblygroupmodule

# Update assembly group module by hierarchy

def update_assemblygroupmodule_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if assembly group exists
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if not assemblygroup:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Then get the assembly group module
    assemblygroupmodule = session.get(AssemblyGroupModule, module_id)
    if not assemblygroupmodule:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=module_id)
        )

    # Verify that the module belongs to the specified assembly group
    if assemblygroupmodule not in assemblygroup.assemblygroupmodules:
        raise HTTPException(
            status_code=404, detail=f"Assembly group module {module_id} not found in assembly group {assemblygroup_id}"
        )

    # Update the module
    assemblygroupmodule.name = input.name
    session.commit()
    log_print("update", obj_id=module_id, obj_type=msg_object_type)
    return assemblygroupmodule

# Delete assembly group module by hierarchy

def delete_assemblygroupmodule_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, session: SessionDependency) -> None:
    # First check if biketype exists
    biketype = session.get(BikeType, biketype_id)
    if not biketype:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=biketype_id)
        )

    # Then check if assembly group exists
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if not assemblygroup:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=assemblygroup_id)
        )

    # Verify that the assembly group belongs to the specified bike type
    if assemblygroup not in biketype.assemblygroups:
        raise HTTPException(
            status_code=404, detail=f"Assembly group {assemblygroup_id} not found in bike type {biketype_id}"
        )

    # Then get the assembly group module
    assemblygroupmodule = session.get(AssemblyGroupModule, module_id)
    if not assemblygroupmodule:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=module_id)
        )

    # Verify that the module belongs to the specified assembly group
    if assemblygroupmodule not in assemblygroup.assemblygroupmodules:
        raise HTTPException(
            status_code=404, detail=f"Assembly group module {module_id} not found in assembly group {assemblygroup_id}"
        )

    # Delete the module
    session.delete(assemblygroupmodule)
    session.commit()
    log_print("delete", obj_id=module_id, obj_type=msg_object_type)
