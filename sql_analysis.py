import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("real_estate.db")

# SQL Query
query = """
SELECT neighborhood,
AVG(price) AS avg_price
FROM properties
GROUP BY neighborhood
"""

# Load query result into DataFrame
df = pd.read_sql_query(query, conn)

print("\nAverage Price by Neighborhood:")
print(df)

# Create chart
plt.figure(figsize=(8, 5))
plt.bar(df["neighborhood"], df["avg_price"])
plt.title("Average Property Price by Neighborhood")
plt.xlabel("Neighborhood")
plt.ylabel("Average Price")
plt.grid(True)

plt.savefig("avg_price_analysis.png")
plt.show()

conn.close()