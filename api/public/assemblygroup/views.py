from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from api.auth.models import User
from api.public.biketype.models import BikeType
from api.public.assemblygroup.models import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components

msg_tags = "Assembly Group"
msg_tags_id = "Assembly Group (by ID)"
msg_description_post = "Create an assembly group."
msg_description_get = "Get the list of all assembly groups."
msg_description_get_id = "Get a specific assembly group based on its ID."
msg_description_delete = "Remove a specific assembly group based on its ID."
msg_description_put = "Edit a specific assembly group based on its ID."


def msg_no_type(i):
    return f"No bike type with id={i}."


def msg_no_item(i):
    return f"No assembly group with id={i}."

# Create assembly group


@router.post("/biketypes/{type_id}/assemblygroups/", response_model=AssemblyGroup, tags=[msg_tags], description=msg_description_post, status_code=status.HTTP_201_CREATED)
def add_assembly_group(type_id: int, input: AssemblyGroupInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroup:
    biketype = session.get(BikeType, type_id)
    if biketype:
        new_assemblygroup = AssemblyGroup.model_validate(input)
        # session.add(new_assemblygroup)
        biketype.assemblygroups.append(new_assemblygroup)
        session.commit()
        session.refresh(new_assemblygroup)
        return new_assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_type(type_id)
        )

# Get assemly groups


@router.get("/assemblygroups", tags=[msg_tags], description=msg_description_get)
def get_assembly_groups(session: SessionDep) -> list:
    query = select(AssemblyGroup)
    return session.exec(query).all()

# Get assemly groups by id


@router.get("/assemblygroups/{id}", response_model=AssemblyGroupOutput, tags=[msg_tags_id], description=msg_description_get_id)
def get_assembly_group_by_id(id: int, session: SessionDep) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))

# Delete assembly group


@router.delete("/assemblygroups/{id}", tags=[msg_tags_id], description=msg_description_delete, status_code=status.HTTP_200_OK)
def remove_assembly_group(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        session.delete(assemblygroup)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id)
        )

# Edit assembly group


@router.put("/assemblygroups/{id}", response_model=AssemblyGroup, tags=[msg_tags_id], description=msg_description_put, status_code=status.HTTP_200_OK)
def edit_assembly_group(id: int, new_assemblygroup: AssemblyGroupInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroup.name = new_assemblygroup.name
        session.commit()
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_item(id))
