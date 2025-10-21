from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import AssemblyGroupMessages
from src.models.user import User
from src.crud.assemblygroup import create_assemblygroup, read_all_assemblygroups, read_assemblygroup, update_assemblygroup, delete_assemblygroup
from src.models.assemblygroup import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = AssemblyGroupMessages()

# Create an assembly group


@router.post("/biketypes/{type_id}/assemblygroups/", response_model=AssemblyGroup, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_an_assembly_group(type_id: int, input: AssemblyGroupInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return create_assemblygroup(id=type_id, input=input, session=session)

# Read all assemly groups


@router.get("/assemblygroups", tags=[swagger_desc.tags], description=swagger_desc.description_read_all)
def read_all_assembly_groups(session: SessionDependency) -> list:
    return read_all_assemblygroups(session=session)

# Read an assemly group


@router.get("/assemblygroups/{id}", response_model=AssemblyGroupOutput, tags=[swagger_desc.tags], description=swagger_desc.description_read)
def read_an_assembly_group(id: int, session: SessionDependency) -> AssemblyGroup:
    return read_assemblygroup(id=id, session=session)

# Update an assembly group


@router.put("/assemblygroups/{id}", response_model=AssemblyGroup, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_an_assembly_group(id: int, new_assemblygroup: AssemblyGroupInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroup:
    return update_assemblygroup(id=id, input=new_assemblygroup, session=session)


# Delete an assembly group


@router.delete("/assemblygroups/{id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_an_assembly_group(id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroup(id=id, session=session)
