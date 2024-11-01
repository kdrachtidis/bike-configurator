from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select

from routers.auth import get_current_user
from db import get_session
from schemas import BikeComponent, BikeComponentOutput, BikeComponentInput, User

router = APIRouter(prefix="/api/biketypes")