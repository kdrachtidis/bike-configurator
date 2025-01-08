from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from api.auth.models import User
from api.public.assemblygroup.models import AssemblyGroup
from api.public.assemblygroupmodule.models import AssemblyGroupModule, AssemblyGroupModuleInput, AssemblyGroupModuleOutput

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
msg_description_put = "Edit a specific assembly group module based on its ID."


def msg_success():
    return f"Assembly group module created successfully."


def msg_no_group(i):
    return f"No assembly group with id={i}."


def msg_no_module(i):
    return f"No assembly group module with id={i}."

# Get all assembly group modules


@router.get("/assemblygroupmodules/", tags=[msg_tags], description=msg_description_get, status_code=status.HTTP_200_OK)
def get_group_modules(session: SessionDep) -> list:
    query = select(AssemblyGroupModule)
    return session.exec(query).all()

# Get an assembly group module based on group ID


@router.get("/assemblygroupmodules/{id}", response_model=AssemblyGroupModuleOutput, tags=[msg_tags_id], description=msg_description_get_group_id)
def get_group_module_by_group_id(id: int, session: SessionDep) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id))

# Add module assigned to assembly group


@router.post("/assemblygroups/{assemblygroup_id}/assemblygroupmodules/", response_model=AssemblyGroupModule, tags=[msg_tags], description=msg_description_post, status_code=status.HTTP_201_CREATED)
def add_group_module(assemblygroup_id: int, input: AssemblyGroupModuleInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    assemblygroup = session.get(AssemblyGroup, assemblygroup_id)
    if assemblygroup:
        assemblygroupmodule = AssemblyGroupModule.model_validate(input)
        # session.add(module)
        assemblygroup.assemblygroupmodules.append(assemblygroupmodule)
        session.commit()
        session.refresh(assemblygroupmodule)
        return assemblygroupmodule
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_group(assemblygroup_id)
        )


# Delete an assembly group module based on group ID


@router.delete("/assemblygroupmodules/{id}", tags=[msg_tags_id], description=msg_description_delete, status_code=status.HTTP_200_OK)
def remove_assemby_group_module(id: int, session: SessionDep, user: User = Depends(get_current_user)) -> None:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        session.delete(assemblygroupmodule)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_module(id)
        )

# Edit assembly group module


@router.put("/assemblygroupmodules/{id}", tags=[msg_tags_id], description=msg_description_put, status_code=status.HTTP_200_OK)
def edit_assembly_group_module(id: int, new_assemblygroupmodule: AssemblyGroupModuleInput, session: SessionDep, user: User = Depends(get_current_user)) -> AssemblyGroupModule:
    assemblygroupmodule = session.get(AssemblyGroupModule, id)
    if assemblygroupmodule:
        assemblygroupmodule.name = new_assemblygroupmodule.name
        session.commit()
        return assemblygroupmodule
    else:
        raise HTTPException(status_code=404, detail=msg_no_module(id))
