
from typing import Optional
from pydantic import BaseModel, Field
import uuid
from datetime import  date



class Tarea(BaseModel):
     title: str
     limit: Optional[date] = None
     created: Optional[date] = None
     done: Optional[bool] = False
     user_id: Optional[str] = None
class TareaUpdate(BaseModel):
     title: Optional[str] = None
     limit: Optional[date] = None
     done: Optional[bool] = None
