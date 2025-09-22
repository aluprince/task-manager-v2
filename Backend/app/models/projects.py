from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    priority = Column(String, nullable=False) #1 means low, 2 means medium and 3 means high
    completed_project = Column(Boolean, default=False)
    deadline = Column(String, nullable=False)
    # Linking each project to the user
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects")
    # Linking each task to project
    tasks = relationship("Tasks", back_populates="project")



