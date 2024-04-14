#!/usr/bin/python3
"""
Script to filter states from the hbtn_0e_0_usa database based on user input.

This script connects to a MySQL database and retrieves states from the states
table where the name matches the user input,
sorting them by ID in ascending order.
"""

import sys
import MySQLdb


def filter_states(username, password, db_name, state_name):
    """
    Retrieve and print states where the name matches the user input.
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)
        cursor = db.cursor()
        query = ("SELECT * FROM states WHERE name = '{:s}'"
                 " ORDER BY id ASC").format(state_name)
        cursor.execute(query)
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
