#!/usr/bin/python3
"""List all states from the database passed as argument, sorted by id."""
import MySQLdb
import sys


def main():
    """Connect to the local MySQL server and print all states by id."""

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=pw, db=db, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
