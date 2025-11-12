from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import AssemblyGroupMessages
from src.models.user import User
from src.crud.assemblygroup import create_assemblygroup, read_all_assemblygroups_by_biketype, read_assemblygroup, read_assemblygroup_by_biketype, update_assemblygroup_by_biketype, delete_assemblygroup_by_biketype
from src.models.assemblygroup import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = AssemblyGroupMessages()


# Read an assembly group


@router.get("/assemblygroups/{id}", response_model=AssemblyGroupOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_an_assembly_group(id: int, session: SessionDependency) -> AssemblyGroup:
    return read_assemblygroup(id=id, session=session)


# Read all assembly groups under a bike type


@router.get("/biketypes/{biketype_id}/assemblygroups", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_assembly_groups_by_biketype(biketype_id: int, session: SessionDependency) -> list:
    return read_all_assemblygroups_by_biketype(biketype_id=biketype_id, session=session)


# Create an assembly group


@router.post("/biketypes/{biketype_id}/assemblygroups/", response_model=AssemblyGroup, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_an_assembly_group(biketype_id: int, input: AssemblyGroupInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return create_assemblygroup(id=biketype_id, input=input, session=session)


# Read an assembly group by bike type


@router.get("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}", response_model=AssemblyGroupOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read, status_code=status.HTTP_200_OK)
def read_assembly_group_by_biketype(biketype_id: int, assemblygroup_id: int, session: SessionDependency) -> AssemblyGroup:
    return read_assemblygroup_by_biketype(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, session=session)


# Update an assembly group by bike type


@router.put("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}", response_model=AssemblyGroup, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_assembly_group_by_biketype(biketype_id: int, assemblygroup_id: int, new_assemblygroup: AssemblyGroupInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return update_assemblygroup_by_biketype(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, input=new_assemblygroup, session=session)


# Delete an assembly group by bike type


@router.delete("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_assembly_group_by_biketype(biketype_id: int, assemblygroup_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroup_by_biketype(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, session=session)
