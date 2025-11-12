from typing import Annotated

from fastapi import Depends, APIRouter, status, HTTPException
from sqlmodel import Session

from src.views.user import get_current_user
from src.utils.database import get_session
from src.utils.openapi_desc import AssemblyGroupModuleMessages
from src.models.user import User
from src.crud.assemblygroupmodule import create_assemblygroupmodule_by_hierarchy, read_assemblygroupmodules_by_hierarchy, read_assemblygroupmodule, read_assemblygroupmodule_by_hierarchy, update_assemblygroupmodule_by_hierarchy, delete_assemblygroupmodule_by_hierarchy
from src.models.assemblygroupmodule import AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

router = APIRouter()
SessionDependency = Annotated[Session, Depends(get_session)]
swagger_desc = AssemblyGroupModuleMessages()


# Read an assembly group module


@router.get("/assemblygroupmodules/{module_id}", response_model=AssemblyGroupModuleOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id)
def read_an_assembly_group_module(module_id: int, session: SessionDependency) -> AssemblyGroupModule:
    return read_assemblygroupmodule(id=module_id, session=session)


# Read assembly group modules by hierarchy


@router.get("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}/assemblygroupmodules", response_model=list[AssemblyGroupModuleOutput], tags=[swagger_desc.tags], description="Read all assembly group modules within the hierarchy")
def read_assembly_group_modules_by_hierarchy(biketype_id: int, assemblygroup_id: int, session: SessionDependency) -> list[AssemblyGroupModule]:
    return read_assemblygroupmodules_by_hierarchy(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, session=session)

# Create an assembly group module by hierarchy


@router.post("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}/assemblygroupmodules/", response_model=AssemblyGroupModule, tags=[swagger_desc.tags], description=swagger_desc.description_create, status_code=status.HTTP_201_CREATED)
def create_assembly_group_module_by_hierarchy(biketype_id: int, assemblygroup_id: int, input: AssemblyGroupModuleInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return create_assemblygroupmodule_by_hierarchy(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, input=input, session=session)


# Read an assembly group module by hierarchy


@router.get("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}/assemblygroupmodules/{module_id}", response_model=AssemblyGroupModuleOutput, tags=[swagger_desc.tags], description=swagger_desc.description_get_group_id, status_code=status.HTTP_200_OK)
def read_assembly_group_module_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, session: SessionDependency) -> AssemblyGroupModule:
    return read_assemblygroupmodule_by_hierarchy(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, module_id=module_id, session=session)


# Update assembly group module by hierarchy


@router.put("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}/assemblygroupmodules/{module_id}", response_model=AssemblyGroupModule, tags=[swagger_desc.tags], description=swagger_desc.description_update, status_code=status.HTTP_200_OK)
def update_assembly_group_module_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, input: AssemblyGroupModuleInput, session: SessionDependency, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return update_assemblygroupmodule_by_hierarchy(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, module_id=module_id, input=input, session=session)


# Delete assembly group module by hierarchy


@router.delete("/biketypes/{biketype_id}/assemblygroups/{assemblygroup_id}/assemblygroupmodules/{module_id}", tags=[swagger_desc.tags], description=swagger_desc.description_delete, status_code=status.HTTP_200_OK)
def delete_assembly_group_module_by_hierarchy(biketype_id: int, assemblygroup_id: int, module_id: int, session: SessionDependency, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroupmodule_by_hierarchy(biketype_id=biketype_id, assemblygroup_id=assemblygroup_id, module_id=module_id, session=session)
