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

popular_three_articles()
popular_authors()
