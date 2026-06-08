#!/usr/bin/python3
"""Display all states matching the argument, safe from SQL injection."""
import MySQLdb
import sys


def main():
    """Connect to the MySQL server and print matching states."""
    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    arg = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=usr, passwd=pw, db=db, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE name = %s "
                "ORDER BY id ASC", (arg,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
