#!/usr/bin/python3
"""
Script to filter states from the hbtn_0e_0_usa database based on user input.

This script connects to a MySQL database and retrieves states from the states
table where the name matches the user input,
sorting them by ID in ascending order.

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the database
    state_name: Name of the state to search for
"""

import sys
import MySQLdb


def filter_states(username, password, db_name, state_name):
    """
    Retrieve and print states where the name matches the user input.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
        state_name (str): Name of the state to search for
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    filter_states(username, password, db_name, state_name)
