from typing import Annotated

from fastapi import Depends, APIRouter, status, HTTPException
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import AssemblyGroupModuleMessages
from src.models.user import User
from src.crud.assemblygroupmodule import create_assemblygroupmodule, read_all_assemblygroupmodules, read_assemblygroupmodules_by_group, read_assemblygroupmodule, update_assemblygroupmodule, delete_assemblygroupmodule
from src.models.assemblygroupmodule import AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = AssemblyGroupModuleMessages()

# Create an assembly group module assigned to an assembly group


@router.post("/assemblygroups/{group_id}/assemblygroupmodules/", response_model=AssemblyGroupModule, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_an_assembly_group_module(group_id: int, input: AssemblyGroupModuleInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return create_assemblygroupmodule(id=group_id, input=input, session=session)

# Read assembly group modules by group ID


@router.get("/assemblygroups/{group_id}/assemblygroupmodules/", response_model=list[AssemblyGroupModuleOutput], tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id)
def read_assembly_group_module_by_group_and_module(group_id: int, session: SessionDependency) -> list[AssemblyGroupModule]:
    return read_assemblygroupmodules_by_group(id=group_id, session=session)

# Read all assembly group modules


@router.get("/assemblygroupmodules/", tags=[swagger_desc.tags], description=swagger_desc.description_read_all, status_code=status.HTTP_200_OK)
def read_all_assembly_group_modules(session: SessionDependency):
    return read_all_assemblygroupmodules(session=session)

# Read an assembly group module


@router.get("/assemblygroupmodules/{module_id}", response_model=AssemblyGroupModuleOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id)
def read_an_assembly_group_module(module_id: int, session: SessionDependency) -> AssemblyGroupModule:
    return read_assemblygroupmodule(id=module_id, session=session)

# Update assembly group module


@router.put("/assemblygroupmodules/{id}", tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_an_assembly_group_module(id: int, input: AssemblyGroupModuleInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return update_assemblygroupmodule(id=id, input=input, session=session)


# Delete an assembly group module


@router.delete("/assemblygroupmodules/{id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_an_assemby_group_module(id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroupmodule(id=id, session=session)
