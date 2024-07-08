from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter(prefix="/api/groups")

# Add assembly group


@router.post("/", response_model=AssemblyGroup, tags=["Assembly groups"])
def add_assembly_group(input: AssemblyGroupInput,
                       session: Session = Depends(get_session)) -> AssemblyGroup:
    new_assemblygroup = AssemblyGroup.from_orm(input)
    session.add(new_assemblygroup)
    session.commit()
    session.refresh(new_assemblygroup)
    return new_assemblygroup


# Get assemly groups

@router.get("/", tags=["Assembly groups"])
def get_assembly_groups(type: str | None = None, session: Session = Depends(get_session)) -> list:
    query = select(AssemblyGroup)
    if type:
        query = query.where(AssemblyGroup.biketype == type)
    return session.exec(query).all()

# Get assemly groups by id

@router.get("/{id}", response_model=AssemblyGroupOutput, tags=["Assembly groups"])
def get_assembly_groups_by_id(id: int, session: Session = Depends(get_session)) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        return assemblygroup
    else:
        raise HTTPException(status_code=404, detail=f"No assembly group with id={id}.")

# Delete assembly group


@router.delete("/{id}", status_code=204, tags=["Assembly groups"])
def remove_assembly_group(id: int, session=Depends(get_session)) -> None:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        session.delete(assemblygroup)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No assembly group with id={id}."
        )

# Edit assembly group


@router.put("/{id}", response_model=AssemblyGroup, tags=["Assembly groups"])
def edit_assembly_group(id: int, new_assemblygroup: AssemblyGroupInput, session: Session = Depends(get_session)) -> AssemblyGroup:
    assemblygroup = session.get(AssemblyGroup, id)
    if assemblygroup:
        assemblygroup.name = new_assemblygroup.name
        assemblygroup.biketype = new_assemblygroup.biketype
        session.commit()
        return assemblygroup
    else:
        raise HTTPException(
            status_code=404, detail=f"No assembly group with id={id}.")
