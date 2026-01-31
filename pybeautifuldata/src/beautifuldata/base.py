from typing import Any

from pydantic import BaseModel


class Metadata(BaseModel):
    name: str
    description: str
    source: str


class DataBundle(BaseModel):
    data: Any
    metadata: Metadata
