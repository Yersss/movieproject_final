import sqlite3

def execute_sql(s):
    con = sqlite3.connect('movies.db')
    with con:
        cur = con.cursor()
        cur.execute(s)

sql = cur.execute("SELECT * FROM Movies")
execute_sql(sql)

results = cur.fetchall()
results2 = cur.fetchall()

print(results)
print(results2)
