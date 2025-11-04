from pydantic import BaseModel
from typing import List


class BaseProjectsResponseModel(BaseModel):
    functional: List[str]
    stack: List[str]
    link: str
