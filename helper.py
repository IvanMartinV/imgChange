import os
import shutil
import config as cf
from typing import Tuple


def check_folder(f_info: str) -> None:
    try:
        os.makedirs(f_info, exist_ok=False)
    except:
        print(f'Folder already exists: {f_info}')


def folders_creator() -> None:
    for folders in cf.new_list:
        check_folder(folders)


def next_name(folder_path: str, base_name: str, extension: str) -> Tuple[str, str]:
    """Encuentra el siguiente número disponible para una imagen."""
    index = 0
    while True:
        nuevo_nombre = f"{index}-{base_name}{extension}"
        ruta_nueva = os.path.join(folder_path, nuevo_nombre)
        if not os.path.exists(ruta_nueva):
            return ruta_nueva, nuevo_nombre
        index += 1


def move_rename() -> None:
    """Check if there is an image, move and rename it automatically based on category keys."""
    for key, category_name in cf.categories.items():
        for extension in [".jpg", ".png", ".webp"]:
            ruta_f = os.path.join(cf.f_origin, f"{key}{extension}")

            if os.path.exists(ruta_f):
                destino_folder = os.path.join(cf.f_origin, category_name)

                os.makedirs(destino_folder, exist_ok=True)

                nueva_ruta, nuevo_nombre = next_name(destino_folder, category_name, extension)
                shutil.move(ruta_f, nueva_ruta)

                print(f"Imagen {ruta_f} movida y renombrada a {nueva_ruta}, con nombre: {nuevo_nombre}")

