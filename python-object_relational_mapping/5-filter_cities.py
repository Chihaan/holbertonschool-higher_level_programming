#!/usr/bin/python3
"""List all cities of a given state, sorted by city id."""
import MySQLdb
import sys


def main():
    """Connect to the MySQL server and print the cities of the given state."""
    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]
    cities = []

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=pw, db=db, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT c.name FROM cities c "
                "INNER JOIN states s ON s.id = c.state_id "
                "WHERE s.name = %s "
                "ORDER BY c.id ASC", (arg,))
    query_rows = cur.fetchall()
    for row in query_rows:
        cities.append(row[0])
    print(", ".join(cities))

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
