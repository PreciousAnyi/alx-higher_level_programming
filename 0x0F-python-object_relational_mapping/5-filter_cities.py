#!/usr/bin/python3
"""
Script to list all cities of a given state from the
hbtn_0e_4_usa database.
"""

import sys
import MySQLdb


def filter_cities(username, password, db_name, state_name):
    """
    Retrieve and print all cities of the given state.

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
        query = "SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE \
                name = %s) ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        cities = [row[0] for row in cursor.fetchall()]
        if cities:
            print(", ".join(cities))
        else:
            sys.exit(1)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        return (e)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    filter_cities(username, password, db_name, state_name)
