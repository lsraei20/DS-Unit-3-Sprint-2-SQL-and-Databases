import psycopg2
import sqlite3

# connection
dbname = 'jhazmbft'
user = 'jhazmbft'
password = 'PtNbAUfJfqoiRf-XSDnDBIVZk04nyUMa'
host = 'drona.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

# creating titanic table(already created and committed)

# curs.execute("""
# CREATE TABLE titanic (
#   Survived BOOLEAN,
#   Pclass SMALLINT,
#   Name VARCHAR(50),
#   Sex VARCHAR(10),
#   Age SMALLINT,
#   SiblingsAndSpousesAboard SMALLINT,
#   ParentsAndChildrenAboard SMALLINT,
#   Fare DECIMAL
# )
# """)


curs.execute("""
COPY titanic(Survived, Pclass, Name, Sex, Age, SiblingsAndSpousesAboard, ParentsAndChildrenAboard, Fare)
FROM '/Users/israel/PycharmProjects/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv'
DELIMITER ','
CSV HEADER;
""")


curs.execute("SELECT * FROM titanic;")
print(curs.fetchall())
