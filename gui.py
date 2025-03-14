from fasthtml.common import *

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
"""
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