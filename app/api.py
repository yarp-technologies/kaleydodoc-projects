from uvicorn import Config, Server
import asyncio
import uuid
from fastapi import FastAPI, Request, Form, UploadFile, File, Body, status
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from core.core_object import Core
from constants.variables import *
from constants.msg import *
from urllib.parse import urlencode
from adittional_modules import *

app = FastAPI()

templates = Jinja2Templates(directory="../templates")

@app.get("/")
async def start_menu(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/file", response_class=FileResponse)
async def download_file(filename: str):
    return FileResponse(os.path.join(FILE_FOLDER, filename), filename=filename)

@app.post("/template", response_class=HTMLResponse)
async def dounload_filled_template(
        request: Request,
        input_file_data: UploadFile = File(default=None),
        input_text_data: str = Form(default=None)
):
    file_path = save_file(input_file_data)
    if file_path is None:
        result = {"request": request,
                  "msg": MISSING_FILE}
        return templates.TemplateResponse("error_msg.html", result)
    regex = prepare_regex(input_text_data)
    filler = Core(file_path, regex).process()
    file = Path(filler).name
    url = f"/file?{urlencode({'filename': file})}"
    result = {"request": request,
              "url": url}
    return templates.TemplateResponse("done_template.html", result)

if __name__ == "__main__":
    config = Config(
        app=app,
        host="0.0.0.0",
        port=7777
    )
    server = Server(config)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.serve())