from pydantic import BaseModel
from typing import Literal

StatusType = Literal["FREE", "OCCUPIED", "RESERVED"]


class PSModel(BaseModel):
    id: int
    status: StatusType = "FREE"
