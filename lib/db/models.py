from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

class User(Base):
    instances = []

    __tablename__ = 'users'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.instances.append(self)

    def __repr__(self):
        return [self.first_name, self.last_name]
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    task = relationship('Task', backref=backref('User'))

class Task(Base):

    __tablename__ = 'tasks'

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return [self.id, self.task]
    
    id = Column(Integer(), primary_key=True)
    task = Column(String())
    user = relationship('User', backref=backref('Task'))


class JoinUserTask(Base):

    __tablename__ = 'joins'

    id = id = Column(Integer(), primary_key=True)
    task = Column(Integer(), ForeignKey('tasks.id'))
    user = Column(Integer(), ForeignKey('users.id'))


    