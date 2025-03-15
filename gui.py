from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import shutil
import os

app = FastAPI()

# Configurar plantillas y archivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carpeta por defecto para imágenes
IMAGE_FOLDER = Path("C:/Users/34619/Pictures/newImagenesGuardadas")
DESTINATIONS = {}

@app.get("/", response_class=HTMLResponse)
async def render_gui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "destinations": DESTINATIONS})

@app.post("/add_destination")
async def add_destination(name: str = Form(...), path: str = Form(...)):
    DESTINATIONS[name] = path
    return {"message": "Destino agregado", "destinations": DESTINATIONS}


@app.post("/move_image", response_class=HTMLResponse)
async def move_image(request: Request, filename: str = Form(...), destination: str = Form(...)):
    if destination in destinations:
        src_path = os.path.join(config.f_origin, filename)  # Ruta original de la imagen
        dest_folder = destinations[destination]  # Carpeta de destino
        dest_path = os.path.join(dest_folder, filename)  # Nueva ruta completa

        # Verifica si el archivo existe antes de moverlo
        if os.path.exists(src_path):
            os.makedirs(dest_folder, exist_ok=True)  # Crea la carpeta si no existe
            shutil.move(src_path, dest_path)  # Mueve la imagen

            message = f"Imagen movida a {dest_path}"
        else:
            message = f"Error: El archivo {filename} no existe en {config.f_origin}"
    else:
        message = f"Error: Destino {destination} no encontrado"

    return templates.TemplateResponse("index.html",
                                      {"request": request, "destinations": destinations, "message": message})





















"""from fasthtml.common import *

app, rt = fast_app()

tasks = []

@rt("/")
def get():
    add_task_form = Form(
        Input(type="text", name="task", placeholder="Add a new task..."),
        Button("Add"),
        method="post",
        action="/add-task",
    )
    add_init_url = Form(
        Input(type="text", name="init_url", placeholder="Put the initial image path")
    )

    task_list = Ul(
        *[
            Li(
                f"{task} ",
                " ",
                A("Delete", herf=f"/delete/{i}"),
            )
            for i, task in enumerate(tasks)
        ],
        id="task-list",
    )

    return Titled("Automatic Name Img Changer ", H1("My Tasks"), add_init_url, add_task_form, task_list)


@rt("/add-task", methods=["post"])
def post(task: str):
    if task:
        tasks.append(task)
    return RedirectResponse(url="/", status_code=303)

@rt("/delete/{index}", methods=["get"])
def delete(index: int):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return RedirectResponse(url="/", status_code=303)


serve()
-------------------
app = FastHTML()

def generate_html():
    return Div(H1("Hello"), P("Some text"), P("Some more text"))


@app.get("/")
def home():
    html_content = []
    for _ in range(5):
        html_content.append(generate_html())
    return  Div(*html_content)

serve()
"""