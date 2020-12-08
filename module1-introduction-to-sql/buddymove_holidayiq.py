import sqlite3
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/andrew-ryabchenko/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.rename(columns={'User Id': 'UserId'}, inplace=True)
connection = sqlite3.connect('./buddymove_holidayiq.sqlite3')

try:
    df.to_sql('main', connection)
except ValueError as err:
    print(err)

cursor = connection.cursor()

cursor.execute('SELECT COUNT(*) FROM main')
rows = cursor.fetchall()[0][0]

cursor.execute('''SELECT COUNT(*) FROM
                (SELECT UserId FROM main WHERE main.Nature>100 AND main.Shopping>100)''')
reviews = cursor.fetchall()[0][0]

cursor.execute('''SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM main''')

avg = cursor.fetchall()[0]

connection.close()

print(f'Rows: {rows}')
print(f'Users with more than 100 reviews for Nature and Shopping category: {reviews}\n')
print('Average number of reviews by category:')
print(f'Sports {avg[0]}, Religious {avg[1]}, Nature {avg[2]}\nTheatre {avg[3]}, Shopping {avg[4]}, Picnic {avg[5]}')

