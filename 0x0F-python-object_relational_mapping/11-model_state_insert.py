#!/usr/bin/python3
'''
adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    # saves into the data base
    session.commit()
    print(Louisiana.id)

    session.close()
