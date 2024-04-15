#!/usr/bin/python3
"""
Script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_id(username, password, db_name, state_name):
    """
    Retrieve and print all State objects from the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if state.name == state_name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    print_state_id(username, password, db_name, state_name)
