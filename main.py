import os
import time
import shutil
import sys

f_orign = r"C:\Users\34619\Desktop\TEST"
f_dest = os.path.join(f_orign, "intento1")

os.makedirs(f_dest, exist_ok=True)


def next_name(extension):
    """Encuentra el siguiente número disponible """
    index = 0
    while True:
        nuevo_nombre = f"imagen{index}{extension}"
        ruta_nueva = os.path.join(f_dest, nuevo_nombre)
        if not os.path.exists(ruta_nueva):
            return ruta_nueva, nuevo_nombre
        index += 1


def move_rename():
    """Check if there is an image, move and rename it automatically """
    for extension in [".jpg", ".png"]:
        ruta_q = os.path.join(f_orign, f"q{extension}")
        if os.path.exists(ruta_q):
            nueva_ruta, nuevo_nombre = next_name(extension)
            shutil.move(ruta_q, nueva_ruta)
            print(f"Imagen movida y renombrada a: {nueva_ruta}, con nombre: {nuevo_nombre}")


print("Programa programeando ....... Presiona Ctrl+C to stopit.")

try:
    while True:
        move_rename()
        time.sleep(27)
except KeyboardInterrupt:
    print("\nStopeado correctamente. =) ")
    sys.exit(0)