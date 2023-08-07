from uvicorn import Config, Server
import asyncio
from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from core.core_object import Core
from constants.msg import *
from urllib.parse import urlencode
from adittional_modules import *
import json

app = FastAPI()

templates = Jinja2Templates(directory="../templates")


@app.get("/")
async def start_menu(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/file", response_class=FileResponse)
async def download_file(filename: str):
    return FileResponse(os.path.join(FILE_FOLDER, filename), filename=filename)

@app.post("/api_module", response_class=FileResponse)
async def convert_file(file: UploadFile = File(None), tags: str = Form(None)):
    file_path = save_file(file)
    if file_path is None:
        return None
    try:
        tags_ = json.loads(tags)
    except:
        return None
    filler = Core(file_path, tags_).process()
    if filler is None:
        return None
    file = Path(filler).name
    return FileResponse(os.path.join(FILE_FOLDER, file), filename=file)


@app.post("/template", response_class=HTMLResponse)
async def dounload_filled_template(
        request: Request,
        input_file_data: UploadFile = File(default=None),
        input_text_data: str = Form(default=None)
):
    file_path = save_file(input_file_data)
    print(file_path)
    if file_path is None:
        result = {"request": request,
                  "msg": MISSING_FILE}
        return templates.TemplateResponse("error_msg.html", result)
    regex = prepare_regex(input_text_data)
    filler = Core(file_path, regex).process()
    print(filler)
    if filler != ErrorType.ok:
        result = {"request": request,
                  "msg": MISSING_FILE + str(filler)}
        return templates.TemplateResponse("error_msg.html", result)
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