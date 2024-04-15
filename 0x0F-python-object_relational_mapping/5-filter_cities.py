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
        cursor.execute('SELECT city.name, state.name\
                        FROM cities as city\
                        INNER JOIN states as state\
                        ON city.state_id = state.id\
                        ORDER BY city.id ASC;')
        cities = cursor.fetchall()
        cities_list = []
        for city in cities:
            if city[1] == state_name:
                cities_list.append(city[0])
        print(", ".join(list(dict.fromkeys(cities_list))))
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
