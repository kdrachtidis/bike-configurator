from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from db import get_session
from api.auth.views import get_current_user
from api.auth.models import User
from api.public.assemblygroup.models import AssemblyGroup
from api.public.assemblygroupmodule.models import AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

SessionDep = Annotated[Session, Depends(get_session)]

# HTTPException details messages


def msg_no_group(i):
    return f"No assembly group with id={i}."


def msg_no_module(i):
    return f"No assembly group module with id={i}."

# Create


def create_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDep) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroupmodule = AssemblyGroupModule.model_validate(input)
        assemblygroup.assemblygroupmodules.append(assemblygroupmodule)
        session.commit()
        session.refresh(assemblygroupmodule)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_group(id)
        )

# Read


def read_all_assemblygroupmodules(session: SessionDep) -> list:
    query = select(AssemblyGroupModule)
    print("Read all assemby group modules.")
    return session.exec(query).all()


def read_assemblygroupmodule(id: int, session: SessionDep) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        print("Read assembly group module with id=", id)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id))

# Update


def update_assemblygroupmodule(id: int, input: AssemblyGroupModuleInput, session: SessionDep) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        assemblygroupmodule.name = input.name
        session.commit()
        return assemblygroupmodule
    else:
        raise HTTPException(status_code=404, detail=msg_no_module(id))

# Delete


def delete_assemblygroupmodule(id: int, session: SessionDep) -> None:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        session.delete(assemblygroupmodule)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id)
        )
