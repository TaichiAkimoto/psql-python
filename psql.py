import psycopg2

dbname = "news"

## This function shows which articles have been accessed the most ##
def popular_three_articles():
    conn = psycopg2.connect("dbname="+dbname)
    cur = conn.cursor()
    cur.execute("select path, count(*) as num from log group by path order by num desc limit 4")
    articles = cur.fetchall()
    result = ""
    for i in range(1, 4):
        slug = articles[i][0].split('/')[2]
        #conn_2 = psycopg2.connect("dbname="+dbname)
        #cur_2 = conn_2.cursor()
        #query = "select title from articles where slug = {}".format(slug)
        #cur_2.execute(query)
        ## TODO cur_2.fetchall() inserted instead of slug ##
        article = "\"" + slug + "\""
        views = articles[i][1]
        result = result + "{} - {} views\n".format(article, views)
        #conn_2.close()
    conn.close()

    print(result)

popular_three_articles()

# 1. What are the most popular three articles of all time? Which articles have been accessed the most?
# Present this information as a sorted list with the most popular article at the top.
# reason code didn't move is that I didn't insert the result to variable.
# How stupid I am.
# "Princess Shellfish Marries Prince Handsome"1201 views
# "Baltimore Ravens Defeat Rhode Island Shoggoths"915 views
# "Political Scandal Ends In Political Scandal"553 views
