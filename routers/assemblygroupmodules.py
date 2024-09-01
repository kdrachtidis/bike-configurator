from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput, AssemblyGroupOutput

router = APIRouter(prefix="/api/assemblygroups")


class BadTripException(Exception):
    pass

# Add module dependent on assembly group


@router.post("/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupModule, tags=["Group Modules"])
def add_group_module(assemblygroup_id: int, assemblygroupmodule_input: AssemblyGroupModuleInput, session: Session = Depends(get_session)) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        new_assemblygroupmodule = AssemblyGroupModule.from_orm(
            assemblygroupmodule_input, update={'assemblygroup_id': assemblygroup_id})
        assemblygroup.groupmodules.append(new_assemblygroupmodule)
        session.commit()
        session.refresh(new_assemblygroupmodule)
        return new_assemblygroupmodule
    else:
        raise HTTPException(status_code=404, detail=f"No module with id={id}.")

# Get group module by id


# @router.get("/{id}", response_model=AssemblyGroupModuleOutput, tags=["Group Modules"])
# def get_module_by_id(id: int, session: Session = Depends(get_session)) -> AssemblyGroupModule:
 #   groupmodule = session.get(AssemblyGroupModule, id)
  #  if groupmodule:
   #     return groupmodule
    # else:
     #   raise HTTPException(
      #      status_code=404, detail=f"No group module with id{id}.")

@router.get("/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupOutput, tags=["Group Modules"])
def get_assembly_modules(assemblygroup_id: int, session: Session = Depends(get_session)) -> AssemblyGroupModule:
    # groupmodule = session.get(AssemblyGroupModule, id)
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        assemblygroup.groupmodules.all()
    else:
        raise HTTPException(
            status_code=404, detail=f"No group module with id{id}.")
