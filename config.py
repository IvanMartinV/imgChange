import json
from pathlib import Path


with open("categorias.json", "r", encoding="utf-8") as file:
    data = json.load(file)

categories = data["categorias"]
f_origin = Path(data["paths"]["f_origin"])


new_list = [str(f_origin)]


for key, value in categories.items():
    new_path = f_origin / value
    new_list.append(str(new_path))

print(new_list)
