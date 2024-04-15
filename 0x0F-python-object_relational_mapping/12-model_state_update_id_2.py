#!/usr/bin/python3
"""
Script to change the name of a State object
in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, db_name):
    """
    Change the name of a State object in the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"

    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
