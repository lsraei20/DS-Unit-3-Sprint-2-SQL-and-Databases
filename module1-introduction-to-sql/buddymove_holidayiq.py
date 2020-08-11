import pandas as pd
import sqlite3
from sqlalchemy import create_engine


engine = create_engine('sqlite://', echo=False)
df = pd.read_csv('/Users/israel/PycharmProjects/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql'
                 '/buddymove_holidayiq.csv')
df.drop('User Id', axis=1, inplace=True)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=engine)

print('\n1-) Count how many rows you have\n')
print('There are ', len(engine.execute("SELECT * FROM review").fetchall()), 'rows\n')

print("2-) How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping\n"
      "category?\n")
print('There are', len(engine.execute('SELECT Nature, Shopping FROM review WHERE Nature >= 100 AND Shopping >= 100')
                       .fetchall()), 'who reviewed 100 or more in the nature and shopping categories\n')
print('3-) What are the average number of reviews for each category?\n')
for col in df.columns:
    print(col, 'column has an average of', engine.execute('SELECT AVG(' + col + ') FROM review').fetchall())
