from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import AssemblyGroup, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput, User

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components
msg_tags = "Assembly Group Module"
msg_tags_id = "Assembly Group Module (by ID)"
msg_description_post = "Add an assembly group module, providing the ID of the assembly group it belongs to."
msg_description_get = "Get the list of all assembly group modules."
msg_description_get_id = "Get a specific assembly group module based on its ID."
msg_description_get_group_id = "Get a specific assembly group module based on its group's and module's ID."
msg_description_delete = "Remove a specific assembly group module based on its ID."


def msg_success():
    return f"Assembly group module created successfully."


def msg_no_group(i):
    return f"No assembly group with id={i}."


def msg_no_match_item(groupinput, groupattr, module):
    return f"Assembly group module with id={module} does not belong to group with id={groupinput}. It belongs to group with id={groupattr}"


def msg_no_module(i):
    return f"No assembly group module with id={i}."

# Get an assembly group module based on group ID


@router.get("/assemblygroups/{group_id}/assemblygroupmodules/{assemblygroupmodule_id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags_id], description=msg_description_get_group_id)
def get_group_module_by_group_id(group_id: int, assemblygroupmodule_id: int, session: SessionDep) -> AssemblyGroupModule:
    module = session.get(AssemblyGroupModule, assemblygroupmodule_id)
    if module and group_id == module.assemblygroup_id:
        return module
    elif module and group_id != module.assemblygroup_id:
        raise HTTPException(
            status_code=404, detail=msg_no_match_item(group_id, module.assemblygroup_id, assemblygroupmodule_id))
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(assemblygroupmodule_id))

# Add module assigned to assembly group


@router.post("/assemblygroups/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupModule, tags=[msg_tags], description=msg_description_post, status_code=status.HTTP_201_CREATED)
def add_group_module(assemblygroup_id: int, assemblygroupmodule_input: AssemblyGroupModuleInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        new_assemblygroupmodule = AssemblyGroupModule.model_validate(
            assemblygroupmodule_input, update={'assemblygroup_id': assemblygroup_id})
        assemblygroup.groupmodules.append(new_assemblygroupmodule)
        session.commit()
        session.refresh(new_assemblygroupmodule)
        return new_assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_group(assemblygroup_id))

# Get all assembly group modules


@router.get("/assemblygroupmodules", tags=[msg_tags], description=msg_description_get)
def get_group_modules(session: SessionDep) -> list:
    query = select(AssemblyGroupModule)
    return session.exec(query).all()

# Delete an assembly group module based on group ID


@router.delete("/assemblygroupmodules/{id}", tags=[msg_tags_id], description=msg_description_delete)
def remove_assemby_group_module(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    module = session.get(AssemblyGroupModule, id)
    if module:
        session.delete(module)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id)
        )

# @router.put("/{}")
