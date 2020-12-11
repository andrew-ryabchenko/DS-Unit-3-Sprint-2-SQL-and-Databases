import sqlite3

# Establish connection
connection = sqlite3.connect('northwind_small.sqlite3')
cursor = connection.cursor()

# Answering the questions Part 2
ans1 = cursor.execute("""
SELECT ProductName FROM Product
ORDER BY UnitPrice DESC LIMIT 10
""").fetchall()

ans2 = cursor.execute("""
SELECT round(AVG(HireDate - BirthDate),1) FROM Employee
""").fetchall()[0][0]

ans3 = cursor.execute("""
SELECT City, round(AVG(HireDate - BirthDate),1) FROM Employee 
GROUP BY City
""").fetchall()

# Answering the questions Part 3

ans4 = cursor.execute("""
SELECT ProductName, SupplierId FROM Product
ORDER BY UnitPrice DESC LIMIT 10
""").fetchall()

ans5 = cursor.execute("""
SELECT CategoryId FROM (SELECT CategoryId, COUNT(DISTINCT ProductName) 
AS prod_count
FROM Product GROUP BY CategoryId ORDER BY prod_count DESC LIMIT 1)
""").fetchall()[0][0]

ans6 = cursor.execute("""
SELECT FirstName, LastName FROM Employee WHERE Employee.ID IN
(SELECT EmployeeId FROM EmployeeTerritory AS et
GROUP BY et.EmployeeId ORDER BY COUNT(TerritoryId) DESC LIMIT 1)
""").fetchall()[0]

connection.close()


print('_______________________________')
print("""What are the ten most expensive items (per unit price) in the database?""")
print(ans1)
print('_______________________________')
print("""What is the average age of an employee at the time of their hiring?""")
print(ans2)
print('_______________________________')
print("""How does the average age of employee at hire vary by city?""")
print(ans3)
print('_______________________________')
print("""What are the ten most expensive items (per unit price) in the database *and* their suppliers?""")
print(ans4)
print('_______________________________')
print("""What is the largest category (by number of unique products in it)?""")
print(ans5)
print('_______________________________')
print("""Who's the employee with the most territories?""")
print(ans6)
print('_______________________________')

# Answering Questions Part 4

# Q. In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
# A. Those two tables are connected on Employee.Id and EmployeeTerritory.EmployeeId

# Q. What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
# A. It would be appropriate to store data in NoSQL database when each instance of that data has its' own unique shape and set of attributes. NoSQL also assumes no relations between object documents. If the data is structured in the tabular format relational database should be used. 

# Q. What is "NewSQL", and what is it trying to achieve?
# A. NewSQL is modern class of relational DBSM that seek to provide NoSQL-like scalability among with ACID guarantees. 