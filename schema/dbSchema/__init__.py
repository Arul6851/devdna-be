from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column,Integer, String,DateTime,JSON,ARRAY, ForeignKey
from datetime import datetime
from db import Base

class SeedList(Base):
    __tablename__ = "seed_list"
    
    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    
class Developer(Base):
    __tablename__ = "developer"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False) 
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())