from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, Annotated

class NoteBase(BaseModel):
    title:Annotated[str, Field(..., title="Title of the note", examples=['Maths','Science'])]
    content:Annotated[str, Field(...)]
    published: bool = True  

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class NoteResponse(NoteBase):
    id : int
    created_at: datetime

    class Config:
        from_attributes = True
