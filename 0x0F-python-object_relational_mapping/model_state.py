#!/usr/bin/python3
'''
contains the class definition of a State
and an instance Base = declarative_base()
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    Class inherits from Base class
    and Links MYSQL table 'state'.

    Instances:
        id: represents a column of an auto-generated, unique integer
        name: represents a column of a string with maximum 128 characters
    '''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
