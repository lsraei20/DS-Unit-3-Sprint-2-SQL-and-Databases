import psycopg2
import sqlite3

# identification information
dbname = 'wlbclegy'
user = 'wlbclegy'
password = 'KPCKVmKdv-uBr8fIKYk3pDBdwdKTybu0'
host = 'isilo.db.elephantsql.com'

# connecting to the server and creating a cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# explore the data base
pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall())

# input values into the data base
pg_curs.execute("""
INSERT INTO test_table (name, data) VALUES
(
    'Zaphod Beeblebrox',
    '{"key": "value", "key2": "true"}'::JSONB
)
""")
pg_curs.execute('SELECT * FROM test_table')
print(pg_curs.fetchall())
pg_conn.commit()

# get data out (list of tuples with all character data
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
sl_curs.execute('SELECT * FROM charactercreator_character;')
characters = sl_curs.fetchall()
print(characters[:4])

# check what types of data there are in the table
sl_curs.execute('PRAGMA table_info(charactercreator_character);')
print(sl_curs.fetchall())

# create a statement for PostgreSQL that uses the data types
# make a new cursor
pg_curs.close()
pg_curs = pg_conn.cursor()
# pg_curs.execute(
#     """
# CREATE TABLE charactercreator_character (
#   character_id SERIAL PRIMARY KEY,
#   name VARCHAR(30),
#   level INT,
#   exp INT,
#   hp INT,
#   strength INT,
#   intelligence INT,
#   dexterity INT,
#   wisdom INT
# );
# """
# )

# load the data!

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

# pg_conn.commit()

# check
pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
print(pg_curs.fetchall())
