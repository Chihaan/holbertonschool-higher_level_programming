#!/usr/bin/python3
"""Print the id of the State matching the given name, or 'Not found'."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Connect and print the matching State id, or 'Not found'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    main()
