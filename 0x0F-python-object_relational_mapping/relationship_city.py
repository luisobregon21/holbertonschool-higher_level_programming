#!/usr/bin/python3
'''
contains the class definition of a State
and an instance Base = declarative_base()
class has relationship with State class
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    '''
    Class inherits from Base class
    and Links MYSQL table 'state'.

    Instances:
        id: represents a column of an auto-generated, unique integer
        name: represents a column of a string with maximum 128 characters
        state_id: that represents a column of an integer
        can’t be null and is a foreign key to states.id
    '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
