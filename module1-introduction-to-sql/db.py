import sqlite3

# In order to run this file rpg_db.sqlite3 should be placed in the directory of this file. 



classes = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
# Establish connection to database
db = sqlite3.connect('./databases/rpg_db.sqlite3')
# Create cursor to execute queries 
cursor = db.cursor()
# Q1.
query = cursor.execute("SELECT COUNT(*) FROM charactercreator_character")
response = query.fetchmany()
print(f'Q. How many total Characters are there?\nA. {response[0][0]}')
print('________________________________________')


# Q2.
print('Q. How many of each specific subclass?')
print('A.')
for item in classes:
    query = cursor.execute(f"SELECT COUNT(*) FROM charactercreator_{item}")
    response = query.fetchall()
    print(f'{response[0][0]} of {item}')
print('________________________________________')

# Q3.
print('Q. How many total Items?')
query = cursor.execute(f"SELECT COUNT(*) FROM armory_item")
response = query.fetchall()
print(f'A. {response[0][0]}')
print('________________________________________')

# Q4.
print('Q. How many of the Items are weapons? How many are not?')
query = cursor.execute("SELECT COUNT(*) FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id=armory_weapon.item_ptr_id")
weapons = query.fetchall()[0][0]
query = cursor.execute("SELECT COUNT(*) FROM armory_item")
tot_items = query.fetchall()[0][0]
print(f'A. {weapons} weapons and {tot_items-weapons} are not weapons')
print('________________________________________')

# Q5. 
print('Q. How many Items does each character have? (Return first 20 rows)')
query = cursor.execute("SELECT character_id, COUNT(*) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20")
response = query.fetchall()
print('A.')
print('(character_id, items_count)')
print('--------------------------')
for item in response:
    print(item)
print('________________________________________')

# Q6.
print('Q. How many Weapons does each character have? (Return first 20 rows)')
query = cursor.execute("""SELECT character_id, COUNT(*) 
                        FROM charactercreator_character_inventory AS cci 
                        WHERE 
                        cci.item_id in (SELECT item_ptr_id FROM armory_weapon) 
                        GROUP BY character_id LIMIT 20""")
response = query.fetchall()
print('A.')
print('(character_id, weapons_count)')
print('--------------------------')
for item in response:
    print(item)
print('________________________________________')

# Q7. 
print('Q. On average, how many Items does each Character have?')
query = cursor.execute("""SELECT AVG(item_count) FROM (SELECT COUNT(item_id) AS item_count
                                                        FROM charactercreator_character_inventory  
                                                        GROUP BY character_id)""")
response = query.fetchall()
print(f'A. {round(response[0][0], 2)}')
print('________________________________________')
#Q8. 
print('Q. On average, how many Weapons does each character have?')
query = cursor.execute("""SELECT AVG(weapon_count) FROM (SELECT COUNT(*) AS weapon_count
                                                        FROM charactercreator_character_inventory AS cci 
                                                        WHERE 
                                                        cci.item_id in (SELECT item_ptr_id FROM armory_weapon) 
                                                        GROUP BY character_id)""") 
response = query.fetchall()
print(f'A. {round(response[0][0], 2)}')
print('________________________________________')

