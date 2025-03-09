import os
import shutil
import config as cf
from typing import Tuple


def check_folder(f_info: str) -> None:
    try:
        os.makedirs(f_info, exist_ok=False)
    except:
        print(f'folder already exist : {f_info}')


def folders_creator() -> None:
    for folders in cf.list:
        check_folder(folders)


def next_name(extension: str) -> Tuple[str, str]:
    """Encuentra el siguiente número disponible """
    index = 0
    while True:
        nuevo_nombre = f"imagen{index}{extension}"
        ruta_nueva = os.path.join(cf.f_d, nuevo_nombre)
        if not os.path.exists(ruta_nueva):
            return ruta_nueva, nuevo_nombre
        index += 1


def move_rename() -> None:
    """Check if there is an image, move and rename it automatically """
    for extension in [".jpg", ".png", ".webp"]:
        ruta_q = os.path.join(cf.f_orign, f"q{extension}")
        if os.path.exists(ruta_q):
            nueva_ruta, nuevo_nombre = next_name(extension)
            shutil.move(ruta_q, nueva_ruta)
            print(f"Imagen movida y renombrada a: {nueva_ruta}, con nombre: {nuevo_nombre}")


