import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('sample.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL query
query = '''
SELECT date, COUNT(DISTINCT account_id) AS dau_count
    FROM account_date_session
    GROUP BY date
    ORDER BY date;

'''
cursor.execute(query)

# Fetch the query result
results = cursor.fetchall()

# Create a DataFrame from the query result
df = pd.DataFrame(results, columns=['date', 'dau_count'])

# Convert 'date' column to datetime format (if not already in datetime format)
df['date'] = pd.to_datetime(df['date'])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['dau_count'], marker='o', linestyle='-')
plt.title('Daily Active Users Over Time')
plt.xlabel('Date')
plt.ylabel('DAU Count')
plt.grid(True)
plt.show()

# Close the cursor and connection
cursor.close()
conn.close()
