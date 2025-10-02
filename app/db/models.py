from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(Integer, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
