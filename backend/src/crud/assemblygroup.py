from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.models.biketype import BikeType
from src.models.assemblygroup import AssemblyGroup, AssemblyGroupInput
from src.utils.logging import log_print, log_exception

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "assembly group"

# Create


def create_assemblygroup(id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    biketype = session.get(BikeType, id)
    if biketype:
        assemblygroup = AssemblyGroup.model_validate(input)
        biketype.assemblygroups.append(assemblygroup)
        session.commit()
        session.refresh(assemblygroup)
        log_print("create", obj_type=msg_object_type)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("type", obj_id=id)
        )

# Read


def read_all_assemblygroups(session: SessionDependency) -> list:
    query = select(AssemblyGroup)
    log_print("read_all", obj_type=msg_object_type)
    return session.exec(query).all()


def read_assemblygroup(id: int, session: SessionDependency) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id))

# Update


def update_assemblygroup(id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroup.name = input.name
        session.commit()
        log_print("update", obj_id=id, obj_type=msg_object_type)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id))

# Delete


def delete_assemblygroup(id: int, session: SessionDependency) -> None:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        session.delete(assemblygroup)
        session.commit()
        log_print("delete", obj_id=id, obj_type=msg_object_type)
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id)
        )
