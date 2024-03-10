from sqlalchemy import create_engine
from models import User, Status, Task
from seed import create_dummy_data

# Create a new engine instance
engine = create_engine('postgresql://postgres:test1234@localhost:5432/hw06')

# Create all tables in the engine
# Base.metadata.create_all(engine)
User.metadata.create_all(engine)
Status.metadata.create_all(engine)
Task.metadata.create_all(engine)

create_dummy_data(engine)

