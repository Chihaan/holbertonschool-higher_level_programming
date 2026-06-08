#!/usr/bin/python3
"""Print the first State object from the database, or 'Nothing' if empty."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Connect to the database and print the first State, or 'Nothing'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    main()
