import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import pycountry

# Connect to the SQLite database
conn = sqlite3.connect('sample.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute the SQL query to get revenue data
user_query = '''
    SELECT country_code, COUNT(DISTINCT account_id) AS user_count
    FROM account WHERE country_code is not null
    GROUP BY country_code ORDER BY user_count DESC LIMIT 50
'''
cursor.execute(user_query)
user_results = cursor.fetchall()

# Convert the results to a Pandas DataFrame
users = pd.DataFrame(user_results, columns=['Country', 'Number of Users'])

print(users)

# Use pycountry to get ISO alpha-3 codes
users['iso_a3'] = users['Country'].apply(lambda x: pycountry.countries.get(alpha_2=x).alpha_3 if pycountry.countries.get(alpha_2=x) else None)

# Import world shape map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge dataframes on the 'iso_a3' column
for_plotting = world.merge(users, left_on='iso_a3', right_on='iso_a3', how='left')

# Fill NaN values with a default value (e.g., 0)
for_plotting['Number of Users'].fillna(0, inplace=True)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 7))

# Plot merged dataframe
for_plotting.plot(column='Number of Users', cmap='Dark2', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Total users by Country"})

# Display the plot
plt.show()
