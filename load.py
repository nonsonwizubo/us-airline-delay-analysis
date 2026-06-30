import pandas as pd
import sqlite3
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "DelayedFlights.csv")

# 1. Load your raw data
df = pd.read_csv(file_path)

# 2. Connect to the database in the same directory
db_path = os.path.join(script_dir, "flights.db")
conn = sqlite3.connect(db_path)

# 3. Push the data into the SQL database
df.to_sql("flights", conn, if_exists="replace", index=False)

# 4. Close the connection
conn.close()

print("Database 'flights.db' created and data loaded successfully!")