from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import AssemblyGroup, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput, AssemblyGroupOutput

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components
msg_tags = "Assembly Group Modules"
msg_description_post = "Add an assembly group module, providing the ID of the assembly group it belongs to."
msg_description_get = "Get the list of all assembly group modules."
msg_description_get_id = "Get a specific assembly group module based on its ID."
msg_description_get_group_id = "Get a specific assembly group module based on its group's and module's ID."

def msg_no_item(i):
    return f"No assembly group with id={i}."

# Add module assigned to assembly group


@router.post("/assemblygroups/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupModule, tags=[msg_tags], description=msg_description_post)
def add_group_module(assemblygroup_id: int, assemblygroupmodule_input: AssemblyGroupModuleInput, session: SessionDep) -> AssemblyGroupModule:
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
            status_code=404, detail=msg_no_item(assemblygroup_id))

# [Temporary] Get all assembly group modules


@router.get("/assemblygroupmodules", tags=[msg_tags], description=msg_description_get)
def get_group_modules(session: SessionDep) -> list:
    query = select(AssemblyGroupModule)
    return session.exec(query).all()

# Get assembly group module based on module ID

# @router.get("/assemblygroupmodules/{id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags], description=msg_description_get_id)
# def get_group_module_by_id(id: int, session: Session = Depends(get_session)) -> AssemblyGroupModule:
#     module = session.get(AssemblyGroupModule, id)
#     if module:
#         return module
#     else:
#          raise HTTPException(
#             status_code=404, detail=msg_no_item(id))

# Get assembly group module based on group ID

@router.get("/assemblygroups/{assemblygroup_id}/assemblygroupmodules/{assemblygroupmodule_id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags], description=msg_description_get_group_id)
def get_group_module_by_group_id(assemblygroup_id: int, assemblygroupmodule_id: int, session: Session = Depends(get_session)) -> AssemblyGroupModule:
    module = session.get(AssemblyGroupModule, assemblygroupmodule_id)
    #assemblygroup_id = "module.assemblygroup_id"
    if module:
        return module
    else:
         raise HTTPException(
            status_code=404, detail=msg_no_item(id))
