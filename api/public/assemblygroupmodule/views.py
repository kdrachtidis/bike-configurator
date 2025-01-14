from typing import Annotated

from fastapi import Depends, APIRouter, status
from sqlmodel import Session

from api.auth.views import get_current_user
from api.utils.db import get_session
from api.auth.models import User
from api.public.assemblygroupmodule.crud import create_assemblygroupmodule, read_all_assemblygroupmodules, read_assemblygroupmodule, update_assemblygroupmodule, delete_assemblygroupmodule
from api.public.assemblygroupmodule.models import AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Swagger UI's descriptions
msg_tags = "Assembly Group Module"
msg_description_create = "Add an assembly group module, providing the ID of the assembly group it belongs to."
msg_description_read_all = "Get the list of all assembly group modules."
msg_description_read = "Get a specific assembly group module based on its ID."
msg_description_get_group_id = "Get a specific assembly group module based on its group's and module's ID."
msg_description_delete = "Remove a specific assembly group module based on its ID."
msg_description_update = "Edit a specific assembly group module based on its ID."

# Create an assembly group module assigned to an assembly group


@router.post("/assemblygroups/{assemblygroup_id}/assemblygroupmodules/", response_model=AssemblyGroupModule, tags=[msg_tags], description=msg_description_create, status_code=status.HTTP_201_CREATED)
def create_an_assembly_group_module(id: int, input: AssemblyGroupModuleInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return create_assemblygroupmodule(id=id, input=input, session=session)


# Read all assembly group modules


@router.get("/assemblygroupmodules/", tags=[msg_tags], description=msg_description_read_all, status_code=status.HTTP_200_OK)
def read_all_assembly_group_modules(session: SessionDep):
    return read_all_assemblygroupmodules(session=session)

# Read an assembly group module


@router.get("/assemblygroupmodules/{id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags], description=msg_description_get_group_id)
def read_an_assembly_group_module(id: int, session: SessionDep) -> AssemblyGroupModule:
    return read_assemblygroupmodule(id=id, session=session)

# Update assembly group module


@router.put("/assemblygroupmodules/{id}", tags=[msg_tags], description=msg_description_update, status_code=status.HTTP_200_OK)
def update_an_assembly_group_module(id: int, input: AssemblyGroupModuleInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    return update_assemblygroupmodule(id=id, input=input, session=session)


# Delete an assembly group module


@router.delete("/assemblygroupmodules/{id}", tags=[msg_tags], description=msg_description_delete, status_code=status.HTTP_200_OK)
def delete_an_assemby_group_module(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    return delete_assemblygroupmodule(id=id, session=session)
