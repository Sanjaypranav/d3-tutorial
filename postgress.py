import psycopg2

conn = psycopg2.connect(host="localhost",database="mydb", user="postgres", password='2509', port=5432)
cur = conn.cursor()

cur.execute("SELECT * FROM test")
print(cur.fetchall())
