import pandas as pd
import sqlite3
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "DelayedFlights.csv")


df = pd.read_csv(file_path)


db_path = os.path.join(script_dir, "flights.db")
conn = sqlite3.connect(db_path)


df.to_sql("flights", conn, if_exists="replace", index=False)

conn.close()

print("Database 'flights.db' created and data loaded successfully!")
