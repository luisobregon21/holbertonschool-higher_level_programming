#!/usr/bin/python3
'''
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
'''


from sys import argv
from sqlalchemy import create_engine, orm
import sqlalchemy
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # create a configured "Session" class
    session = orm.sessionmaker(bind=engine)()

    states = session.query(State).order_by(State.id)

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
