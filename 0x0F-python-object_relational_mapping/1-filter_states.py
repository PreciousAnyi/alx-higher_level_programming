#!/usr/bin/python3
"""
Script to list states with names starting with 'N' from the
hbtn_0e_0_usa database.

This script connects to a MySQL database and retrieves states whose names start
with 'N' (uppercase) from the states table,
sorting them by ID in ascending order.

Usage:
    ./1-filter_states.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the database
"""

import sys
import MySQLdb


def filter_states(username, password, db_name):
    """
    Retrieve and print states with names starting with 'N'.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                       " ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except Exception as e:
        return (e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    filter_states(username, password, db_name)
