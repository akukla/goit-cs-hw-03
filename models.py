from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True)

    tasks = relationship('Task', backref=backref('user'))

class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    tasks = relationship('Task', backref='status')

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    status_id = Column(Integer, ForeignKey('status.id'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
