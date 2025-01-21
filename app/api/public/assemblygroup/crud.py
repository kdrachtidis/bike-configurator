from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.api.utils.database import get_session
from app.api.public.biketype.models import BikeType
from app.api.public.assemblygroup.models import AssemblyGroup, AssemblyGroupInput

SessionDependency = Annotated[Session, Depends(get_session)]

# Logs
msg_init = "Bike Configurator API"  # API logs identifier
msg_create = ": Create assembly group."
msg_read_all = ": Read all assemby groups."
msg_read = ": Read assembly group with id ="
msg_update = ": Update assembly group with id ="
msg_delete = ": Delete assembly group with id ="

# HTTPException details messages


def msg_no_type(i):
    return f"No bike type with id={i}."


def msg_no_item(i):
    return f"No assembly group with id={i}."

# Create


def create_assemblygroup(id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    biketype = session.get(BikeType, id)
    if biketype:
        assemblygroup = AssemblyGroup.model_validate(input)
        biketype.assemblygroups.append(assemblygroup)
        session.commit()
        session.refresh(assemblygroup)
        print(msg_init, end="")
        print(msg_create)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_type(id)
        )

# Read


def read_all_assemblygroups(session: SessionDependency) -> list:
    query = select(AssemblyGroup)
    print(msg_init, end="")
    print(msg_read_all)
    return session.exec(query).all()


def read_assemblygroup(id: int, session: SessionDependency) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        print(msg_init, end="")
        print(msg_read, id)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Update


def update_assemblygroup(id: int, input: AssemblyGroupInput, session: SessionDependency) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroup.name = input.name
        session.commit()
        print(msg_init, end="")
        print(msg_update, id)
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Delete


def delete_assemblygroup(id: int, session: SessionDependency) -> None:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        session.delete(assemblygroup)
        session.commit()
        print(msg_init, end="")
        print(msg_delete, id)
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id)
        )
