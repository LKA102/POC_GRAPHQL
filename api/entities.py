import strawberry
from typing import List


@strawberry.type
class Publicacion:
    id: int
    titulo: str
    autor: str
    categoria: str
    descripcion: str
    publicada: bool
    etiquetas: List[str]


@strawberry.type
class Movie:
    title: str
    director: str
