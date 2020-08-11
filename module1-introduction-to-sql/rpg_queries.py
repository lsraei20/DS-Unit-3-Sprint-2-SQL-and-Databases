import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


print('1-) How many total Characters are there?\n')
curs.execute('SELECT * FROM charactercreator_character;')
print('There are', len(curs.fetchall()), 'total characters\n')


print('2-) How many of each specific subclass?\n')
char_types = ['fighter', 'necromancer', 'thief', 'mage', 'cleric']
for char in char_types:
    curs.execute('SELECT * FROM charactercreator_' + char)
    print('There are', len(curs.fetchall()), char + 's')


print('\n3-) How many total Items?\n')
curs.execute('SELECT * FROM armory_item;')
print('There are', len(curs.fetchall()), 'items\n')


print('4-) How many of the Items are weapons? How many are not?\n')
curs.execute('SELECT * FROM armory_weapon;')
weapons = len(curs.fetchall())
print(weapons, 'items are weapons')
curs.execute('SELECT * FROM armory_item;')
all_items = len(curs.fetchall())
print(all_items - weapons, 'are non-weapon items\n')


print('5-) How many Items does each character have? (Return first 20 rows)\n')
curs.execute('SELECT name, num_of_items FROM charactercreator_character AS cc INNER JOIN (SELECT character_id, '
             'COUNT(*) AS num_of_items FROM charactercreator_character_inventory GROUP BY 1) AS ic ON  '
             'cc.character_id = ic.character_id LIMIT 20;')
print('Character name & number of items it has', curs.fetchall())


print('\n6-) How many Weapons does each character have? (Return first 20 rows)\n')
curs.execute('SELECT name, COALESCE(num_of_weapons, 0) as num_of_weapons FROM (SELECT name, num_of_weapons FROM ('
             'SELECT * FROM charactercreator_character AS cc LEFT JOIN (SELECT character_id, COUNT(*) AS '
             'num_of_weapons FROM (SELECT cc.character_id, cc.item_id FROM charactercreator_character_inventory AS '
             'cc, armory_weapon AS aw WHERE cc.item_id = aw.item_ptr_id) GROUP BY 1) AS ccc ON cc.character_id = '
             'ccc.character_id)) LIMIT 20;')
print('Character name & number of weapons it has', curs.fetchall())


print('\n7-) On average, how many Items does each Character have?\n')
curs.execute('SELECT AVG(num_of_items) FROM (SELECT name, num_of_items FROM charactercreator_character AS cc INNER '
             'JOIN (SELECT character_id, COUNT(*) AS num_of_items FROM charactercreator_character_inventory GROUP BY '
             '1) AS ic ON  cc.character_id = ic.character_id)')
print('Each character has an average of', curs.fetchall(), 'items\n')

print('8-) On average, how many Weapons does each character have?\n')
curs.execute('SELECT AVG(num_of_weapons) FROM (SELECT name, COALESCE(num_of_weapons, 0) as num_of_weapons FROM ('
             'SELECT name, num_of_weapons FROM (SELECT * FROM charactercreator_character AS cc LEFT JOIN (SELECT '
             'character_id, COUNT(*) AS num_of_weapons FROM (SELECT cc.character_id, cc.item_id FROM '
             'charactercreator_character_inventory AS cc, armory_weapon AS aw WHERE cc.item_id = aw.item_ptr_id) '
             'GROUP BY 1) AS ccc ON cc.character_id = ccc.character_id)))')
print('Each character has an average of', curs.fetchall(), 'weapons')
