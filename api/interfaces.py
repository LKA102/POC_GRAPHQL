import strawberry
from typing import Optional


@strawberry.input
class PublicacionFilter:
    autor: Optional[str] = None
    categoria: Optional[str] = None
    publicada: Optional[bool] = None
