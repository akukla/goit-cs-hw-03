from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User, Status, Task

def create_dummy_data(engine):
    # Create a new Faker instance
    fake = Faker()

    # # Create a new engine instance
    # engine = create_engine('postgresql://postgres:test1234@localhost:5432/hw06')

    # Create a new sessionmaker instance
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    if session.query(Status).count() > 0:
        return


    for status_type in ['new', 'in progress', 'completed']:
        status = Status(
            name=status_type
        )
        session.add(status)

    session.commit()


    # Generate random data for users table
    for _ in range(100):  # Generate 100 users
        user = User(
            fullname=fake.name(),
            email=fake.email()
        )
        session.add(user)

    # Generate random data for tasks table
    for _ in range(1000):  # Generate 1000 tasks
        task = Task(
            title=fake.sentence(),
            description=fake.text(),
            status_id=fake.random_int(min=1, max=3),
            user_id=fake.random_int(min=1, max=100)
        )
        session.add(task)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()