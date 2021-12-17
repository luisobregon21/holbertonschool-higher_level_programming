#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa
that contain the letter 'a'
'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, orm
import sqlalchemy

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    session = orm.sessionmaker(bind=engine)()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        if ('a' in state.name):
            print("{}: {}".format(state.id, state.name))

    session.close()
