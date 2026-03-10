from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum, auto
from datetime import date

app = FastAPI()


class Material(Enum):
    BRONCE = auto()
    PLATA = auto()
    ORO = auto()


class Caballero(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelation: str


caballeros = [
    Caballero(id=1, name="Goku", material=Material.ORO, attack=90, constelation="Sayayin"),
    Caballero(id=2, name="Shiryu", material=Material.BRONCE, attack=85, constelation="Dragon"),
]

@app.get("/caballeros")
def showCaballero():
    return caballeros

@app.post("/fight")
def fightCaballero(caballero: Caballero):
    resultado = f"{caballero.name} ataca con poder {caballero.attack}"
    return {"resultado": resultado}

@app.post("/constelation")
def showConstellation(caballero: Caballero):
    return {"constelation": caballero.constelation}


@app.get("/your-caballero")
def showYourCaballero(fecha: date):
    resul= fecha.day % len(caballeros)
    return caballeros[resul]