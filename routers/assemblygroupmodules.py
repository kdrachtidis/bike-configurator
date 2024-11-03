from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput, AssemblyGroupOutput

router = APIRouter(prefix="/api/assemblygroups")

description_post = "Add an assembly group module, providing the ID of the assembly group it belongs to."

# Add module dependent on assembly group


@router.post("/{assemblygroup_id}/assemblygroupmodules", response_model=AssemblyGroupModule, tags=["Group Modules"], description=description_post)
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
            status_code=404, detail=f"No assembly group with id={assemblygroup_id}.")
