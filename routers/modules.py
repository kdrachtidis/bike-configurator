from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput, GroupModule, GroupModuleInput, GroupModuleOutput

router = APIRouter(prefix="/api/modules")

class BadTripException(Exception):
    pass

# Add module


@router.post("/{assemblygroup_id}/groupmodules", response_model=GroupModule, tags=["Group Modules"])
def add_group_module(assemblygroup_id: int, module_input: GroupModuleInput, session: Session = Depends(get_session)) -> GroupModule:
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        new_module = GroupModule.from_orm(
            module_input, update={'assemblygroup_id': assemblygroup_id})
        assemblygroup.groupmodules.append(new_module)
        session.commit()
        session.refresh(new_module)
        return new_module
    else:
        raise HTTPException(status_code=404, detail=f"No module with id={id}.")
