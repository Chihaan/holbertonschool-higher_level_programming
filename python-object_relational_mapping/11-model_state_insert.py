#!/usr/bin/python3
"""Add the State 'Louisiana' to the database and print its new id."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Connect to the database, insert Louisiana, and print its id."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)

    session.close()


if __name__ == "__main__":
    main()
