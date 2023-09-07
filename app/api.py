from uvicorn import Config, Server
import asyncio
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from auth import guest
from auth import api_guest
from users import user
from users import api_user
from links import link


app = FastAPI()

templates = Jinja2Templates(directory="../templates")

app.include_router(guest.router)
app.include_router(api_guest.router)
app.include_router(user.router)
app.include_router(api_user.router)
app.include_router(link.router)

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

if __name__ == "__main__":
    config = Config(
        app=app,
        host="0.0.0.0",
        port=7777
    )
    server = Server(config)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.serve())