import sqlite3
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "flights.db")

# 1. Connect to the existing database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 2. Write your SQL query
query = """
SELECT UniqueCarrier, 
       AVG(ArrDelay) AS avg_arrival_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY UniqueCarrier
ORDER BY avg_arrival_delay DESC;
"""

# 3. Execute and Print the results
results = cur.execute(query).fetchall()

print(f"{'Carrier':<10} | {'Avg Delay':<15} | {'Total Flights'}")
print("-" * 40)
for row in results:
    print(f"{row[0]:<10} | {row[1]:<15.2f} | {row[2]}")

# 4. Close the connection
conn.close()