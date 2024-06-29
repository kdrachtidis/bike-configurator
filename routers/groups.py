from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from db import get_session
from schemas import AssemblyGroup, AssemblyGroupInput, AssemblyGroupOutput

router = APIRouter(prefix="/api/groups")

# Add assembly group


@router.post("/", response_model=AssemblyGroup, tags=["Assembly groups"])
def add_assembly_group(group_input: AssemblyGroupInput,
                       session: Session = Depends(get_session)) -> AssemblyGroup:
    new_group = AssemblyGroup.from_orm(group_input)
    session.add(new_group)
    session.commit()
    session.refresh(new_group)
    return new_group


# Get assemly groups

@router.get("/", tags=["Assembly groups"])
def get_assembly_groups(session: Session = Depends(get_session)) -> list:
    query = select(AssemblyGroup)
    return session.exec(query).all()

# Delete assembly group


@router.delete("/{id}", status_code=204, tags=["Assembly groups"])
def remove_assembly_group(id: int, session=Depends(get_session)) -> None:
    group = session.get(AssemblyGroup, id)
    if group:
        session.delete(group)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"No assembly group with id={id}."
        )

@router.put("/{id}", response_model=AssemblyGroup, tags=["Assembly groups"])
def edit_assembly_group(id: int, new_data: AssemblyGroupInput, session: Session = Depends(get_session)) -> AssemblyGroup:
    group = session.get(AssemblyGroup, id)
    if group:
        group.name = new_data.name
        session.commit()
        return group
    else:
        raise HTTPException(status_code=404, detail=f"No assembly group with id={id}.")