import sqlite3
import pandas as pd

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
    a.created_time BETWEEN '2016-01-01' AND '2016-12-31'
GROUP BY
    a.country_code
ORDER BY avg_revenue_per_user DESC;
'''
cursor.execute(query)

# Fetch the query result
results = cursor.fetchall()

# Specify the file path using double backslashes or a raw string
filepath = r'D:\Jobs\SuperCell-Data Intern\file.xlsx'

# Convert the result to a DataFrame
df = pd.DataFrame(results, columns=['Country', 'User count','Average revenue per user'])

# Save the DataFrame to Excel
df.to_excel(filepath, index=False)

# Close the database connection
conn.close()
