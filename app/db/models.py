from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    hashed_pwd = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Is the user admin?
    is_admin = Column(Boolean, default=False)
    # Is owned by the admin of the account
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    patients = relationship("User", backref="owner", remote_side=[id])

    #used for soft delete on delete_user_services
    is_deleted = Column(Boolean, default=False)
    deletion_date = Column(DateTime, nullable=True)