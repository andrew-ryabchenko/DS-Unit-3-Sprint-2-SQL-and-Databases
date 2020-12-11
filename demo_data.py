import sqlite3

# Establish connection to the database
connection = sqlite3.connect('./demo_data.sqlite3')
cursor = connection.cursor()

# Create table
try:
    cursor.execute("""CREATE TABLE demo(s VARCHAR(10), x INT, y INT)""")
    connection.commit()

except sqlite3.OperationalError as err:
    print(err)

# Prepare data for inserting
data = {'s':['g','v','f'],
        'x':[3,5,8],
        'y':[9,7,7]}

# Insert data
for i in range(3):
    s = data['s'][i]
    x = data['x'][i]
    y = data['y'][i]
    cursor.executemany("INSERT INTO demo (s,x,y) VALUES (?, ?, ?)", [(s,x,y)])
    connection.commit()

# Answer questions

ans1 = cursor.execute('SELECT COUNT(*) FROM demo').fetchall()[0][0]
ans2 = cursor.execute("""SELECT COUNT(*) FROM demo 
                         WHERE x>=5 AND y>=5""").fetchall()[0][0]
ans3 = cursor.execute('SELECT COUNT(DISTINCT y) FROM demo').fetchall()[0][0]

print(f'demo table has {ans1} rows')
print(f'demo table has {ans2} rows where both x and y are at least 5')
print(f'unique values of `y` {ans3}')

# Close connection 
connection.close()


