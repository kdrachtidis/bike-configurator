from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter(prefix="/api/assemblygroups")
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components

msg_tags = "Assembly Groups"
msg_description_post = "Add an assembly group."
msg_description_get = "Get the list of all assembly groups."
msg_description_get_id = "Get a specific assembly group based on its ID."
msg_description_delete = "Remove a specific assembly group based on its ID."
msg_description_put = "Edit a specific assembly group based on its ID."


def msg_no_item(i):
    return f"No assembly group with id={i}."

# Add assembly group


@router.post("/", response_model=AssemblyGroup, tags=[msg_tags], description=msg_description_post)
def add_assembly_group(input: AssemblyGroupInput, session: SessionDep) -> AssemblyGroup:
    new_assemblygroup = AssemblyGroup.model_validate(input)
    session.add(new_assemblygroup)
    session.commit()
    session.refresh(new_assemblygroup)
    return new_assemblygroup


# Get assemly groups

@router.get("/", tags=[msg_tags], description=msg_description_get)
def get_assembly_groups(type: str | None = None, session: Session = Depends(get_session)) -> list:
    query = select(AssemblyGroup)
    if type:
        query = query.where(AssemblyGroup.biketype == type)
    return session.exec(query).all()

# Get assemly groups by id


@router.get("/{id}", response_model=AssemblyGroupOutput, tags=[msg_tags], description=msg_description_get_id)
def get_assembly_group_by_id(id: int, session: SessionDep) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Delete assembly group


@router.delete("/{id}", status_code=204, tags=[msg_tags], description=msg_description_delete)
def remove_assembly_group(id: int, session: SessionDep) -> None:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        session.delete(assemblygroup)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id)
        )

# Edit assembly group


@router.put("/{id}", response_model=AssemblyGroup, tags=[msg_tags], description=msg_description_put)
def edit_assembly_group(id: int, new_assemblygroup: AssemblyGroupInput, session: SessionDep) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroup.name = new_assemblygroup.name
        assemblygroup.biketype = new_assemblygroup.biketype
        session.commit()
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))
