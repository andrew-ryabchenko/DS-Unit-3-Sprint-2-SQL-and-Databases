"""This code will transfer .csv dataset to the PostgresSQL table"""

HOST = 'otto.db.elephantsql.com'
USER, DATABASE = 'oqovqoyz', 'oqovqoyz' 
PASSWORD = 'lKFHnpOHJBoVNVH-DNd81C4I-z2jK2PE'

import psycopg2 as pg
import pandas as pd
from sqlalchemy.types import *
import sqlalchemy

#Import Dataset
df = pd.read_csv('https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
df['PassengerID'] = [i for i in range(0, len(df))]

#Establish connection to database
connection=sqlalchemy.create_engine('postgres://oqovqoyz:lKFHnpOHJBoVNVH-DNd81C4I-z2jK2PE@otto.db.elephantsql.com:5432/oqovqoyz').connect()

# Our titanic database will contain 4 tables linked by PassengerID. FOREIGN KEY constraint will be set on all of the tables 
# to protect integrity of the data ;=)

# Tables:
    # 'bio' table will contain PassengerID (PRIMARY KEY), Name, Sex, Age attributes for each row
    # 'relatives_aboard' table will contain PassengerID (FOREIGN KEY), Siblings/Spouses Aboard, and Parents/Children Aboard
    # 'ticket_details' table will contain PassengerID (FOREIGN KEY), Pclass, and Fare
    # 'survival_status' table will contain PassengerID (FOREIGN KEY) and Survived

# Create subsets of df 
bio = df[['PassengerID','Name','Sex','Age']]
relatives_aboard=df[['PassengerID','Siblings/Spouses Aboard','Parents/Children Aboard']]
ticket_details=df[['PassengerID','Pclass','Fare']]
survival_status=df[['PassengerID','Survived']]

# Populate database with subsets
bio.to_sql('bio', connection, if_exists='replace')
relatives_aboard.to_sql('relatives_aboard', connection, if_exists='replace')
ticket_details.to_sql('ticket_details', connection, if_exists='replace')
survival_status.to_sql('survival_status', connection, if_exists='replace')

connection.close()