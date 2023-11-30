import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('sample.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL query
query = '''
SELECT
    a.country_code AS market,
    COUNT(DISTINCT a.account_id) AS user_count,
    SUM(i.iap_price_usd_cents) / COUNT(DISTINCT a.account_id) AS avg_revenue_per_user
FROM
    account a
JOIN
    iap_purchase i ON a.account_id = i.account_id
WHERE
    a.created_time BETWEEN '2016-01-01' AND '2016-12-31' AND a.country_code is not null
GROUP BY
    a.country_code
ORDER BY avg_revenue_per_user DESC;
'''
cursor.execute(query)

# Fetch the query result
results = cursor.fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(results, columns=['Country', 'User count','Average revenue per user'])

# Close the database connection
conn.close()

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(df['Country'], df['Average revenue per user'], color='blue', alpha=0.7)
plt.xlabel('Country')
plt.ylabel('Average Revenue per User')
plt.title('Average Revenue per User by Country')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for better spacing
plt.show()
