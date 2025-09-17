from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from src.utils.database import get_session
from src.models.assemblygroup import AssemblyGroup
from src.models.assemblygroupmodule import AssemblyGroupModule, AssemblyGroupModuleInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_init = "Bike Configurator API"  # API logs identifier
msg_create = ": Create assembly group module."
msg_read_all = ": Read all assemby group modules."
msg_read = ": Read assembly group module with id ="
msg_update = ": Update assembly group module with id ="
msg_delete = ": Delete assembly group module with id ="

# HTTPException details messages


def msg_no_group(i):
    return f"No assembly group with id={i}."


def msg_no_module(i):
    return f"No assembly group module with id={i}."

# Create


def create_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroupmodule = AssemblyGroupModule.model_validate(input)
        assemblygroup.assemblygroupmodules.append(assemblygroupmodule)
        session.commit()
        session.refresh(assemblygroupmodule)
        print(msg_init, end="")
        print(msg_create)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_group(id)
        )

# Read


def read_all_assemblygroupmodules(session: SessionDependency) -> list:
    query = select(AssemblyGroupModule)
    print(msg_init, end="")
    print(msg_read_all)
    return session.exec(query).all()


def read_assemblygroupmodule(id: int, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        print(msg_init, end="")
        print(msg_read, id)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id))

# Update


def update_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDependency) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        assemblygroupmodule.name = input.name
        session.commit()
        print(msg_init, end="")
        print(msg_update, id)
        return assemblygroupmodule
    else:
        raise HTTPException(status_code=404, detail=msg_no_module(id))

# Delete


def delete_assemblygroupmodule(id: int, session: SessionDependency) -> None:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        session.delete(assemblygroupmodule)
        session.commit()
        print(msg_init, end="")
        print(msg_delete, id)
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id)
        )
