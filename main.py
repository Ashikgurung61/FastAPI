from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_302_FOUND

app = FastAPI()

# Set up template directory
templates = Jinja2Templates(directory="templates")

# Dummy user credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

@app.get("/", response_class=HTMLResponse)
def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        response = RedirectResponse(url="/dashboard", status_code=HTTP_302_FOUND)
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
