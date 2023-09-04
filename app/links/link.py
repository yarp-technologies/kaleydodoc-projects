from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.modules.user_modules import *

router = APIRouter(
    prefix="/link",
    tags=["link"],
)

@router.get("/file", response_class=FileResponse)
async def download_file(filename: str):
    file_path = os.path.join(FILE_FOLDER, filename)
    return FileResponse(file_path, filename=filename)