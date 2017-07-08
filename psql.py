import psycopg2

dbname = "news"

conn = psycopg2.connect("dbname="+dbname)
cur = conn.cursor()
cur.execute("select * from articles")
articles = cur.fetchall()
conn.close()

print(articles)
print("I have a good feeling about this")
