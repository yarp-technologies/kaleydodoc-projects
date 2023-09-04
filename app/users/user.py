from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
from app.dependencies.oauth2 import *
from app.modules.user_modules import *
from core.core_object import Core

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_current_user)]
)
database = DBManager("PDF_placeholder", "users")
templates = Jinja2Templates(directory="../templates")
executor = ThreadPoolExecutor(max_workers=4)

@router.post("/tags")
async def upload_docx(current_user: Annotated[dict, Depends(get_current_user)], file: UploadFile = File(...)):
    file_path = save_file(file)
    tags = get_tags(file_path)
    await database.update_field_by_nickname(current_user["nickname"],
                                            "files_docx",
                                            {file.filename: file_path},
                                            transform_user)
    return JSONResponse(content=tags)

@router.post("/placeholder_process", response_class=HTMLResponse)
async def process_data(data: dict, current_user: Annotated[dict, Depends(get_current_user)]):
    filename = data.get("filename")
    del data["filename"]
    username = current_user["nickname"]
    file_path = await database.find_by_nickname(username)
    file_path = file_path["files_docx"][filename]
    # file_size = os.stat(file_path).st_size
    # future = executor.submit(Core(file_path, data).process)
    filler = Core(file_path, data).process()
    file = Path(filler).name
    await database.update_field_by_nickname(current_user["nickname"],
                                            "files_pdf",
                                            {"_".join(file.split("_")[1::]): filler},
                                            transform_user)
    url = f"/link/file?{urlencode({'filename': file})}"
    result = {"url": url}
    return JSONResponse(content=result)

