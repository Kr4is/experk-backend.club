from pydantic import BaseModel
from typing import AnyStr


class HelloSchema(BaseModel):
    error: bool
    message: AnyStr
