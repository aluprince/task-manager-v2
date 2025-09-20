from .user import User
from .tasks import Tasks
from ..db import Base, engine

# Creating all Tables in the database
Base.metadata.create_all(bind=engine)


