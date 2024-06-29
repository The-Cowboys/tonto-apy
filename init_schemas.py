# este archivo se usa para ebitar los errores de importaciones circulares
from pydantic import TypeAdapter
from cowboys.schemas import CowboyRespuesta
from titulos.schemas import TituloRespuesta

def init_schemas():
    TypeAdapter(TituloRespuesta)
    TypeAdapter(CowboyRespuesta)