from typing import List

from pydantic import BaseModel


class NERRequest(BaseModel):
    text: str


class Entity(BaseModel):
    id: int
    text: str
    label: str


class NERResult(BaseModel):
    entities: List[Entity]
    html: str
