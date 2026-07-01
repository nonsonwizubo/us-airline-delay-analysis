import sqlite3
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "flights.db")


conn = sqlite3.connect(db_path)
cur = conn.cursor()


query = """
SELECT UniqueCarrier, 
       AVG(ArrDelay) AS avg_arrival_delay,
       COUNT(*) AS total_flights
FROM flights
GROUP BY UniqueCarrier
ORDER BY avg_arrival_delay DESC;
"""


results = cur.execute(query).fetchall()

print(f"{'Carrier':<10} | {'Avg Delay':<15} | {'Total Flights'}")
print("-" * 40)
for row in results:
    print(f"{row[0]:<10} | {row[1]:<15.2f} | {row[2]}")

conn.close()
