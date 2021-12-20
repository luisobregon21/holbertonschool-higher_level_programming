#!/usr/bin/python3
'''
creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
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

    new_city = City(name='San Francisco')
    new_state = State(name='California', cities=[new_city])
    session.add(new_city, new_state)
    session.commit()
    session.close()
