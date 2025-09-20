from sqlalchemy import Integer, Boolean, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base

class Tasks(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(String)
    # Foreign key for linking tasks to owner
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="tasks")

    

