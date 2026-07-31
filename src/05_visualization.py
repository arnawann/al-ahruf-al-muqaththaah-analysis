# ==========================================
# AL-AHRUF AL-MUQATHTHAAH ANALYSIS
# Visualization
# ==========================================

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

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

# ==========================================
# SECTION 1
# DISTRIBUTION OF MUQATHTHAAH PATTERNS
# ==========================================

pattern_counts = df['Pattern'].value_counts()

plt.figure(figsize=(8,5))

pattern_counts.plot(kind="bar")

plt.title("Distribution of Muqaththaah Patterns")

plt.xlabel("Pattern")

plt.ylabel('Frequency')

plt.tight_layout()

plt.show()