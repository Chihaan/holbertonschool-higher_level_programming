#!/usr/bin/python3
"""List all City objects with their state name, sorted by city id."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def main():
    """Connect to the database and print each city with its state name."""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    main()
