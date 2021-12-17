#!/usr/bin/python3
'''
script that changes the name of a State
object from the database hbtn_0e_6_usa
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

    modify = session.query(State).get(2)
    modify.name = 'New Mexico'
    # saves into the data base
    session.commit()

    session.close()
