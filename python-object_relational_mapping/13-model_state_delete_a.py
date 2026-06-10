#!/usr/bin/python3
"""Delete all State objects whose name contains the letter 'a'."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Connect to the database and delete states whose name has an 'a'."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
