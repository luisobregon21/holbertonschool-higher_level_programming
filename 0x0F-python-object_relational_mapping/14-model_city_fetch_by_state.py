#!/usr/bin/python3
'''
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
'''

# sqlalchemy imports
from sqlalchemy import create_engine, orm
import sqlalchemy

from sys import argv

# Class imports
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # create a configured "Session" class
    session = orm.sessionmaker(bind=engine)()

    cities = (session
              .query(State.name, City.id, City.name)
              .filter(City.state_id == State.id)
              .order_by(City.id))

    for city in cities:
        print("{}: ({}) {}".format(*city))

    session.close()
