import os
import json
import shutil
import threading
import time
import re
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import config
import helper

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configurar plantillas y archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Cargar categorías desde el JSON
def load_categories():
    with open("categorias.json", "r", encoding="utf-8") as file:
        return json.load(file)["categorias"]


categories = dict(sorted(load_categories().items()))  # Ordenar al cargar


def normalize_key(filename):
    """Extrae la clave del archivo, ignorando números y espacios en paréntesis (ej: 'm (1).jpg' -> 'm')."""
    return re.sub(r"\s*\(\d+\)", "", filename).split(".")[0]


def check_and_move_images():
    """Verifica si hay imágenes nuevas y las mueve automáticamente."""
    while True:
        for filename in os.listdir(config.f_origin):
            src_path = Path(config.f_origin) / filename
            if src_path.is_file():
                key = normalize_key(filename)  # Obtener clave sin paréntesis ni números
                if key in categories:
                    category_name = categories[key]
                    category_folder = Path(config.f_origin) / category_name
                    os.makedirs(category_folder, exist_ok=True)

                    new_filename, dest_path = helper.next_name(str(category_folder), category_name, src_path.suffix)
                    shutil.move(str(src_path), dest_path)
                    print(f"✅ Imagen {filename} movida como {new_filename} a {category_folder}")
        time.sleep(2)  # Esperar 2 segundos antes de la siguiente verificación


# Iniciar el proceso automático en segundo plano
threading.Thread(target=check_and_move_images, daemon=True).start()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Carga la página principal con las categorías ordenadas."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "categories": dict(sorted(categories.items()))  # Mantener ordenadas las categorías
    })


@app.post("/add_category", response_class=HTMLResponse)
async def add_category(request: Request, shortcut: str = Form(...), folder_name: str = Form(...)):
    """Añade una nueva categoría al JSON y crea la carpeta correspondiente."""
    # Solo agregamos la categoría si no existe
    if shortcut not in categories:
        categories[shortcut] = folder_name

        # Guardar en categorias.json
        with open("categorias.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["categorias"][shortcut] = folder_name
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()

    # Crear la carpeta si no existe
    category_folder = Path(config.f_origin) / folder_name
    os.makedirs(category_folder, exist_ok=True)

    # Recargar las categorías actualizadas
    categories.update(load_categories())
    categories_sorted = dict(sorted(categories.items()))

    return templates.TemplateResponse("index.html", {
        "request": request,
        "categories": categories_sorted  # Pasar categorías ordenadas a la interfaz
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
