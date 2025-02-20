from fastapi import APIRouter, Request, Form, Depends, Cookie
from sqlmodel import Session
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.utils.database import get_session
from app.views.bikecomponent import read_all_bike_components

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request, cookie: str | None = Cookie(None)):
    print(cookie)
    return templates.TemplateResponse("home.html",
                                      {"request": request})


@router.post("/search", response_class=HTMLResponse)
def search(*, source: str = Form(...), group: str = Form(...),
           request: Request,
           session: Session = Depends(get_session)):
    components = read_all_bike_components(
        source=source, group=group, session=session)
    return templates.TemplateResponse("search_results.html",
                                      {"request": request, "components": components})
