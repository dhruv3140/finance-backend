from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users" # This is the actual table name in the database

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, default="viewer") # roles: admin, analyst, viewer
    status = Column(String, default="active") # active or inactive
# --- Record Model (Your Code, slightly updated) ---
class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    amount = Column(Float) 
    type = Column(String)      
    category = Column(String)   
    description = Column(String, nullable=True) 
    timestamp = Column(DateTime(timezone=True), server_default=func.now())