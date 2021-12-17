#!/usr/bin/python3
'''
table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=user, passwd=password,
                                 db=db_name)
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT cities.id, cities.name, states.name
                   FROM cities INNER JOIN states
                   on cities.state_id = states.id
                   ''')

    # fetches all rows of a query result set and returns as tuple
    q_rows = cursor.fetchall()
    for row in q_rows:
        print(row)
    cursor.close()
    connection.close()
