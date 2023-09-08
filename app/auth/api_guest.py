from fastapi import APIRouter, Form
from app.dependencies.oauth2 import *
from fastapi.security import OAuth2PasswordRequestForm


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/api",
    tags=["api"]
)
database = DBManager("PDF_placeholder", "users")

@router.post("/signup")
async def sign_up(
        name: str = Form(...),
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...)
):
    '''
    API user's registration
    :param name: insert name (example: user1) (required)
    :param username: insert username (example: user_first) (required)
    :param email: insert email (example: example@mail.ru) (required)
    :param password: insert password (example: 12345) (required)
    :return: response registration (example: {"msg": "You're registered"})
    '''
    if await database.find_by_nickname(username):
        return {"msg": "You're already registered"}
    else:
        user = {
            "name": name,
            "nickname": username,
            "email": email,
            "key": hashed.hash_password(password),
            "files_docx": {},
            "files_pdf": {}
        }
        await database.add_user(user)
        return {"msg": "You're registered"}

@router.post("/access_token")
async def sign_in(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    '''
    Get API user's access token
    :param username: insert username (example: user_first) (required)
    :param password: insert password (example: 12345) (required)
    :return:
    '''
    users = await authenticate_user(form_data.username, form_data.password)
    if not users:
        return {"access_token": "", "token_type": "Bearer", "response": False}
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer", "response": True}
