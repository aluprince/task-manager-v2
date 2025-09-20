from sqlalchemy import Column, Integer ,String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    # Linking each tasks to the user and cascade deletes all tasks when user is deleted
    tasks = relationship("Tasks", back_populates="owner", cascade="all, delete-orphan")
    # Linking refresh token to the user
    refresh_token = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token_hash = Column(String, nullable=False, unique=True)  # store hash of the raw token
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked = Column(Boolean, default=False)
    replaced_by = Column(String, nullable=True)  # token_hash of rotated token (if any)
    user = relationship("User", back_populates="refresh_token")