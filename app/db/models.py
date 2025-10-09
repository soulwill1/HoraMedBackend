from sqlalchemy import Column, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    hashed_pwd = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    owner_id = Column(String(36), ForeignKey("users.id"), nullable=True)

    patients = relationship("User", backref="owner", remote_side=[id])

    is_deleted = Column(Boolean, default=False)
    deletion_date = Column(DateTime, nullable=True)
