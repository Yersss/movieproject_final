import sqlite3

def execute_sql(s):
    con = sqlite3.connect('movies.db')
    with con:
        cur = con.cursor()
        cur.execute(s)

movie_list = []
