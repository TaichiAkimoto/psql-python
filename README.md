# psql-python
PostgreSQL test using python.

## How to use
This project is unavailable for you.
If you do not have the same PostgreSQL database on your local or remote machine,
query of this code fetches 0 result.

## Libraries used
**psycopg2** is used for accessing PostgreSQL.

## Query
1. Query for each articles.title, counted order is how many articles.slug matches log.path. Two tables connected.
2. Query for each authors.name, counted order is the same with 1. Three tables connected.
3. Add three new views.
  * First view is to convert log.time with regular date expression like "July 26, 2016".
  * Second view is number of errors for each converted date.
  * Third view is number of logs for each converted date.
  * Lastly select result with date and error/log ratio.
