from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from api.auth.views import get_current_user
from db import get_session
from api.auth.models import User
from api.public.assemblygroup.crud import create_assemblygroup, read_all_assemblygroups, read_assemblygroup, update_assemblygroup, delete_assemblygroup
from api.public.assemblygroup.models import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Swagger UI's descriptions
msg_tags = "Assembly Group"
msg_description_create = "Create an assembly group."
msg_description_read_all = "Get the list of all assembly groups."
msg_description_read = "Get a specific assembly group based on its ID."
msg_description_delete = "Remove a specific assembly group based on its ID."
msg_description_update = "Edit a specific assembly group based on its ID."

# Create an assembly group


@router.post("/biketypes/{type_id}/assemblygroups/", response_model=AssemblyGroup, tags=[msg_tags], description=msg_description_create, status_code=status.HTTP_201_CREATED)
def create_an_assembly_group(type_id: int, input: AssemblyGroupInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return create_assemblygroup(id=type_id, input=input, session=session)

# Read all assemly groups


@router.get("/assemblygroups", tags=[msg_tags], description=msg_description_read_all)
def read_all_assembly_groups(session: SessionDep) -> list:
    return read_all_assemblygroups(session=session)

# Read an assemly group


@router.get("/assemblygroups/{id}", response_model=AssemblyGroupOutput, tags=[msg_tags], description=msg_description_read)
def read_an_assembly_group(id: int, session: SessionDep) -> AssemblyGroup:
    return read_assemblygroup(id=id, session=session)

# Update an assembly group


@router.put("/assemblygroups/{id}", response_model=AssemblyGroup, tags=[msg_tags], description=msg_description_update, status_code=status.HTTP_200_OK)
def update_an_assembly_group(id: int, new_assemblygroup: AssemblyGroupInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return update_assemblygroup(id=id, input=new_assemblygroup, session=session)


# Delete an assembly group


@router.delete("/assemblygroups/{id}", tags=[msg_tags], description=msg_description_delete, status_code=status.HTTP_200_OK)
def delete_an_assembly_group(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroup(id=id, session=session)
