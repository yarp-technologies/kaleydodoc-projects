from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.dependencies.oauth2 import *


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
database = DBManager("PDF_placeholder", "users")
hashed = PasswordManager()
templates = Jinja2Templates(directory="../templates")

@router.get("/signup", response_class=HTMLResponse)
async def sign_up(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})

@router.post("/signup", response_class=HTMLResponse)
async def sign_up(
        request: Request,
        name: str = Form(...),
        nickname: str = Form(...),
        email: str = Form(...),
        password: str = Form(...)
):
    if await database.find_by_nickname(nickname):
        return templates.TemplateResponse("sign_up.html",
                                          {"request": request, "msg": "Пользователь уже существует"})
    else:
        user = {
            "name": name,
            "nickname": nickname,
            "email": email,
            "key": hashed.hash_password(password),
            "files_docx": {},
            "files_pdf": {}
        }
        await database.add_user(user)
        return templates.TemplateResponse("sign_in.html", {"request": request})

#Todo: версия с oauth2, jwt и с хэшированием паролей

@router.get("/signin", response_class=HTMLResponse)
async def sign_in(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})

@router.post("/signin", response_class=HTMLResponse)
async def sign_in(
        request: Request,
        nickname: str = Form(...),
        password: str = Form(...)
):
    user = authenticate_user(nickname, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": nickname}, expires_delta=access_token_expires
    )
    result = {
        "request": request,
        "access_token": access_token,
        "nickname": nickname
    }
    return templates.TemplateResponse("pdf_placeholder.html", result)


@router.post("/api_signin")
async def sign_in(
        username: str,
        password: str
):
    users = authenticate_user(username, password)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer"}
