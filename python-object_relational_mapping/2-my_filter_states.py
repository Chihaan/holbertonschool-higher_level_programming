#!/usr/bin/python3
"""Display all states whose name matches the argument given."""
import MySQLdb
import sys


def main():
    """Connect to the local MySQL server and print the matching states."""

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=pw, db=db)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY = '{}' "
                "ORDER BY states.id ASC".format(arg))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
