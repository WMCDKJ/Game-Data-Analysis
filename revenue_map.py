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
revenue_query = '''
    SELECT a.country_code, SUM(i.iap_price_usd_cents) AS Total_revenue
    FROM account a
    JOIN iap_purchase i ON a.account_id = i.account_id WHERE a.country_code is not null
    GROUP BY a.country_code ORDER BY Total_revenue DESC
'''
cursor.execute(revenue_query)
revenue_results = cursor.fetchall()

# Convert the results to a Pandas DataFrame
revenue = pd.DataFrame(revenue_results, columns=['Country', 'TotalRevenue'])

print(revenue)

# Use pycountry to get ISO alpha-3 codes
revenue['iso_a3'] = revenue['Country'].apply(lambda x: pycountry.countries.get(alpha_2=x).alpha_3 if pycountry.countries.get(alpha_2=x) else None)

# Import world shape map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge dataframes on the 'iso_a3' column
for_plotting = world.merge(revenue, left_on='iso_a3', right_on='iso_a3', how='left')

# Fill NaN values with a default value (e.g., 0)
for_plotting['TotalRevenue'].fillna(0, inplace=True)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 7))

# Plot merged dataframe
for_plotting.plot(column='TotalRevenue', cmap='jet', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Total Revenue by Country"})

# Display the plot
plt.show()
