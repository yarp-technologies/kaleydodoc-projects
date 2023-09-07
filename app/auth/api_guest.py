from fastapi import APIRouter
from app.dependencies.oauth2 import *
from fastapi.security import OAuth2PasswordRequestForm


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/api",
    tags=["api"]
)
database = DBManager("PDF_placeholder", "users")

@router.post("/access_token")
async def sign_in(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    users = await authenticate_user(form_data.username, form_data.password)
    if not users:
        return {"access_token": "", "token_type": "Bearer", "response": False}
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer", "response": True}
