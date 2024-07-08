from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

router = APIRouter(prefix="/api/modules")


class BadTripException(Exception):
    pass

# Add module


@router.post("/{assemblygroup_id}/groupmodules", response_model=AssemblyGroupModule, tags=["Group Modules"])
def add_group_module(assemblygroup_id: int, module_input: AssemblyGroupModuleInput, session: Session = Depends(get_session)) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        new_module = AssemblyGroupModule.from_orm(
            module_input, update={'assemblygroup_id': assemblygroup_id})
        assemblygroup.groupmodules.append(new_module)
        session.commit()
        session.refresh(new_module)
        return new_module
    else:
        raise HTTPException(status_code=404, detail=f"No module with id={id}.")

# Get group module by id


@router.get("/{id}", response_model=AssemblyGroupModuleOutput, tags=["Group Modules"])
def get_module_by_id(id: int, session: Session = Depends(get_session)) -> AssemblyGroupModule:
    groupmodule = session.get(AssemblyGroupModule, id)
    if groupmodule:
        return groupmodule
    else:
        raise HTTPException(
            status_code=404, detail=f"No group module with id{id}.")
