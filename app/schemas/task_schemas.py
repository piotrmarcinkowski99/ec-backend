from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class TaskSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    completed: bool = False
