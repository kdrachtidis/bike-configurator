from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.models.assemblygroup import AssemblyGroup
from src.models.assemblygroupmodule import AssemblyGroupModule, AssemblyGroupModuleInput
from src.utils.logging import log_print, log_exception

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_object_type = "assembly group module"

# Create


def create_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroupmodule = AssemblyGroupModule.model_validate(input)
        assemblygroup.assemblygroupmodules.append(assemblygroupmodule)
        session.commit()
        session.refresh(assemblygroupmodule)
        log_print("create", obj_type=msg_object_type)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id)
        )

# Read


def read_all_assemblygroupmodules(session: SessionDependency) -> list:
    query = select(AssemblyGroupModule)
    log_print("read_all", obj_type=msg_object_type)
    return session.exec(query).all()


def read_assemblygroupmodules_by_group(id: int, session: SessionDependency) -> list:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        log_print("read_by_group", group_id=id, obj_type=msg_object_type)
        return assemblygroup.assemblygroupmodules
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("group", obj_id=id)
        )


def read_assemblygroupmodule(id: int, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        log_print("read", obj_id=id, obj_type=msg_object_type)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=id))

# Update


def update_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        assemblygroupmodule.name = input.name
        session.commit()
        log_print("update", obj_id=id, obj_type=msg_object_type)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=id))

# Delete


def delete_assemblygroupmodule(id: int, session: SessionDependency) -> None:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        session.delete(assemblygroupmodule)
        session.commit()
        log_print("delete", obj_id=id, obj_type=msg_object_type)
    else:
        raise HTTPException(
            status_code=404, detail=log_exception("module", obj_id=id)
        )
