from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.asgi import GraphQL
from typing import List, Optional

from entities import Movie, Publicacion
from helpers import publicaciones_principales, publicaciones_secundarias, movies_data
from interfaces import PublicacionFilter
from utilities import map_dict_to_publicacion


# This Query class defines the GraphQL API, it is the root of the schema
# Defines what clients can query, defines the API
@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        # Fetch movies from a data source (e.g., database, API)
        return movies_data

    @strawberry.field
    def publicaciones(
        self, filtro: Optional[PublicacionFilter] = None
    ) -> List[Publicacion]:
        data = publicaciones_principales + publicaciones_secundarias

        if filtro:
            if filtro.autor:
                data = [p for p in data if p["autor"] == filtro.autor]
            if filtro.categoria:
                data = [p for p in data if p["categoria"] == filtro.categoria]
            if filtro.publicada is not None:
                data = [p for p in data if p["publicada"] == filtro.publicada]

        return [map_dict_to_publicacion(p) for p in data]


schema = strawberry.Schema(query=Query)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Welcome to the Movie API!"}


app.add_route("/graphql", GraphQL(schema=schema, debug=True))
