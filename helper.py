import os
import shutil

f_orign = r"C:\Users\34619\Desktop\TEST"
f_d = r"C:\Users\34619\Desktop\test2"
f_d_2 = r"C:\Users\34619\Desktop\test3"
list = [f_orign, f_d, f_d_2]


def check_folder(f_info):
    try:
        os.makedirs(f_info, exist_ok=False)
    except:
        print(f'folder already exist : {f_info}')


def folders_creator():
    for folders in list:
        check_folder(folders)


def next_name(extension):
    """Encuentra el siguiente número disponible """
    index = 0
    while True:
        nuevo_nombre = f"imagen{index}{extension}"
        ruta_nueva = os.path.join(f_d, nuevo_nombre)
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


