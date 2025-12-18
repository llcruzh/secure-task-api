from pydantic import BaseModel, Field
from typing import Literal, Optional

Status = Literal["todo", "in_progress", "done"]

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=500)
    status: Status = "todo"
    priority: int = Field(default=3, ge=1, le=5)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[Status] = None
    priority: Optional[int] = Field(default=None, ge=1, le=5)

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: Status
    priority: int

    class Config:
        from_attributes = True
