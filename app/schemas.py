from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------------------------------
# USER SCHEMAS
# ---------------------------------

# 1. This is what the user sends to us when creating an account
class UserCreate(BaseModel):
    name: str
    role: str = "viewer"  # Default role if they don't provide one

# 2. This is what we send back to the user (includes the ID)
class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    status: str

    class Config:
        from_attributes = True # This tells Pydantic to read data from our SQLAlchemy database models

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    description: Optional[str] = None

class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    description: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True 