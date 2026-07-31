import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arnawan1",
    database="al_ahruf_analysis"
)

query = """
SELECT *
FROM muqaththaah;
"""

df = pd.read_sql(query, connection)

print(df.head())

connection.close()