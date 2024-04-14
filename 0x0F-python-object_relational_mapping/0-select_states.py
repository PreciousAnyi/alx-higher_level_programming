#!/usr/bin/python3
"""
Script to list all states from the hbtn_0e_0_usa database.

This script connects to a MySQL database and retrieves all states
from the states table, sorting them by ID in ascending order.

Usage:
    ./select_states.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the database
"""

import sys
import MySQLdb


def get_states(username, password, db_name):
    """
    Retrieve and print all states from the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY ID ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    get_states(username, password, db_name)
