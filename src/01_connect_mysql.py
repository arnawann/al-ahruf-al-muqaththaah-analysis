import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arnawan1",
    database="al_ahruf_analysis"
)

print("✅ Connected to MySQL!")