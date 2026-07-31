# ==========================================
# DATABASE CONNECTION
# ==========================================

import mysql.connector
import pandas as pd

def load_data():
    """
    Load data from MySQL into a Pandas DataFrame.
    """

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

    connection.close()

    return df