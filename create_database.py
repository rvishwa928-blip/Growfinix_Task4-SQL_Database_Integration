import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("real_estate.db")
cursor = conn.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS properties")

# Create table
cursor.execute("""
CREATE TABLE properties (
    id INTEGER PRIMARY KEY,
    neighborhood TEXT,
    size_sqft INTEGER,
    bedrooms INTEGER,
    price INTEGER
)
""")

# Sample data
data = [
    (1, 'Downtown', 1200, 2, 7500000),
    (2, 'Uptown', 1500, 3, 9200000),
    (3, 'Suburb', 1800, 3, 8500000),
    (4, 'Downtown', 1100, 2, 7000000),
    (5, 'Uptown', 1600, 4, 11000000)
]

# Insert data
cursor.executemany(
    "INSERT INTO properties VALUES (?, ?, ?, ?, ?)",
    data
)

# Save changes
conn.commit()

# Display table data
df = pd.read_sql_query(
    "SELECT * FROM properties",
    conn
)

print("\nProperties Table:")
print(df)

# Close connection
conn.close()

print("\nDatabase created successfully!")