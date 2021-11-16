
from sql import create_connection, execute_read_query

conn = create_connection('twe.db')

q = "SELECT name, tweet, link from tweets"

twee = execute_read_query(conn, q)
for user in twee:
    print(user)