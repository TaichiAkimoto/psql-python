import psycopg2

dbname = "news"

## This function shows which articles have been accessed the most ##
def popular_three_articles():
    conn = psycopg2.connect("dbname="+dbname)
    cur = conn.cursor()
    cur.execute("select articles.title, count(*) as num from articles join log on log.path like concat('%', articles.slug) group by articles.title order by num desc limit 3")
    articles = cur.fetchall()
    conn.close()
    result = ''
    for i in range(0, 3):
        result = result + "\"" + articles[i][0] + "\" - " + str(articles[i][1]) + " views\n"
    print("*** What are the most popular three articles of all time?  ***")
    print(result)

def popular_authors():
    conn = psycopg2.connect("dbname="+dbname)
    cur = conn.cursor()
    cur.execute("select authors.name, count(log.path) as num from authors join articles on authors.id = articles.author join log on log.path like concat('%', articles.slug) group by authors.name order by num desc")
    authors = cur.fetchall()
    conn.close()
    result = ''
    for i in range(0, len(authors)):
        result = result + authors[i][0] + " - " + str(authors[i][1]) + " views\n"
    print("*** Who are the most popular article authors of all time?   ***")
    print(result)

def error_days():
    conn = psycopg2.connect("dbname="+dbname)
    cur = conn.cursor()
    cur.execute("create view time_status as select to_char(time, 'FMMonth DD,YYYY') as date, status from log")
    cur.execute("create view error_table as select date, count(status) as errors from time_status where status like '404%' group by date")
    cur.execute("create view log_table as select date, count(status) as logs from time_status group by date")
    cur.execute("select error_table.date, error_table.errors*100/cast(log_table.logs as float) from error_table join log_table on error_table.date = log_table.date where error_table.errors*100/cast(log_table.logs as float) > 1.0")
    errors = cur.fetchall()
    conn.close()
    result = ''
    for i in range(0, len(errors)):
        result = result + errors[i][0] + " - " + str(round(errors[i][1], 2)) + "% errors \n"
    if result == '':
        result = "No big error occured"
    print("*** On which days did more than 1% of requests lead to errors? ***")
    print(result)

popular_three_articles()
popular_authors()
error_days()
