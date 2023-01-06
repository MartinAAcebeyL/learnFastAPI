from fastapi import FastAPI
from enum import Enum
from app.request import Person

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# el orden importa
# cuando se haga una cosulta el de abajo pensara que
# user_id es 'me' y dara un error,
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
# creando path's con valores pre definidos


class LengujesProgracion(str, Enum):
    py = "python"
    js = "javascript"
    rb = "ruby"
    cpp = "c++"
    c = "c"
    java = "java"
    cobol = "cobol"


@app.get("/lenguajes/{lenguaje}")
async def lenguajes_programacion(lenguaje: LengujesProgracion):
    if lenguaje.value == "python":
        return {"lenguaje": lenguaje, "extension": ".py"}
    if lenguaje == LengujesProgracion.js:
        return {"lenguaje": lenguaje, "extension": ".js"}
    if lenguaje == LengujesProgracion.rb:
        return {"lenguaje": lenguaje, "extension": ".rb"}
    if lenguaje == LengujesProgracion.cpp:
        return {"lenguaje": lenguaje, "extension": ".cpp"}
    if lenguaje == LengujesProgracion.c:
        return {"lenguaje": lenguaje, "extension": ".c"}
    if lenguaje.value == "java":
        return {"lenguaje": lenguaje, "extension": ".java"}
    if lenguaje == LengujesProgracion.cobol:
        return {"lenguaje": lenguaje, "extension": ".cobol"}
    return {"lenguaje": lenguaje, "extension": "no encontrado"}


@app.post("/person")
def create_person(person: Person):
    return person