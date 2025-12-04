from enum import IntEnum
from pydantic import BaseModel


class Priority(IntEnum):
    niski = 1
    średni = 2
    wysoki = 3


class Response(BaseModel):
    summary: str
    content: str


class MessageResponse(BaseModel):
    priority: Priority
    summary: str
    responses: list[Response]
