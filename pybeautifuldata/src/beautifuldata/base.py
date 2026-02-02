from typing import Any

import requests
from pydantic import BaseModel


class Metadata(BaseModel):
    name: str
    description: str
    source: str


class DataBundle(BaseModel):
    data: Any
    metadata: Metadata


def load_data_bundle(path: str) -> dict:
    prefix = "https://raw.githubusercontent.com/spectalizer/beautiful-data/main/data/"
    response = requests.get(prefix + path)
    bundle_dict = response.json()
    return bundle_dict
