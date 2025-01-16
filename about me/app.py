from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory="templates")

# Обслуживание статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/blog", response_class=HTMLResponse)
def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@app.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})

