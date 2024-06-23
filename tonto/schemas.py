from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date


# crear un cowboy
class NuevoTonto (BaseModel):
    cowboy_id:int

    class Config:
        from_attributes = True


class TontoRespuesta (BaseModel):
    cowboy_id:int
    created:datetime
    dia:date

    class Config:
        from_attributes = True