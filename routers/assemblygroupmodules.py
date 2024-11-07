from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import AssemblyGroup, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput, AssemblyGroupOutput

router = APIRouter()

# Reusable components
msg_tags = "Assembly Group Modules"
msg_description_post = "Add an assembly group module, providing the ID of the assembly group it belongs to."


def msg_no_item(i):
    return f"No assembly group with id={i}."

# Add module assigned to assembly group

@router.post("/api/assemblygroups/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupModule, tags=[msg_tags], description=msg_description_post)
def add_group_module(assemblygroup_id: int, assemblygroupmodule_input: AssemblyGroupModuleInput, session: Session = Depends(get_session)) -> AssemblyGroupModule:
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

@router.get("/api/assemblygroupmodules", tags=[msg_tags])
def get_group_modules(session: Session = Depends(get_session)) -> list:
    query = select(AssemblyGroupModule)
    return session.exec(query).all()

# Get assembly group module based on group ID

@router.get("/api/assemblygroups/{assemblygroup_id}/assemblygroupmodules/{assemblygroupmodule_id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags])
def get_group_module_by_id(assemblygroup_id: int, assemblygroupmodule_id: int, session: Session = Depends(get_session)) -> AssemblyGroup:
    module = session.get(AssemblyGroupModule, assemblygroup_id, assemblygroupmodule_id)
    if module:
        return module
    else:
         raise HTTPException(
            status_code=404, detail=msg_no_item(id))