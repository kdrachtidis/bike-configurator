from typing import Annotated

from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import BikeType, TestObject, TestObjectInput, TestObjectOutput

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]

# Reusable components
msg_tags = "Test Object"
msg_tags_id = "Test Object (by ID)"


def msg_success():
    return f"Assembly group module created successfully."


def msg_no_group(i):
    return f"No biketype with id={i}."


def msg_no_match_item(groupinput, groupattr, module):
    return f"Assembly group module with id={module} does not belong to group with id={groupinput}. It belongs to group with id={groupattr}"


def msg_no_module(i):
    return f"No assembly group module with id={i}."


@router.post("/biketypes/{biketype_id}/testobjects", response_model=TestObject, tags=[msg_tags_id])
def add_test_object_by_biketype_id(biketype_id: int, testobject_input: TestObjectInput, session: SessionDep) -> TestObject:
    biketype = session.get(BikeType, biketype_id)
    if biketype:
        new_testobject = TestObject.model_validate(
            testobject_input, update={'biketype_id': biketype_id}
        )
        biketype.groups.append(new_testobject)
        session.commit()
        session.refresh(new_testobject)
        return new_testobject
    else:
        raise HTTPException(
            status_code=404, detail=msg_no_group
        )
