#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.

This script connects to a MySQL database and retrieves all
cities from the cities table, along with their corresponding
states, sorting them by city ID in ascending order.

Usage:
    ./4-cities_by_state.py <username> <password> <database-name>
"""

import sys
import MySQLdb


def list_cities(username, password, db_name):
    """
    Retrieve and print all cities from the database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Name of the database
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)
        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states ON \
                        cities.state_id = states.id")
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        return (e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_cities(username, password, db_name)
