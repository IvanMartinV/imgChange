from fasthtml.common import *

app, rt = fast_app(live=True)

@rt('/')
def get():
    return H5('Hello worldddd')


print("Programa programeando ....... Presiona Ctrl+C to stopit.")
