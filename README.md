# Game-Data-Analysis

The 'sample' database is in a zipped file in sqlite3 format. It contains the data of a gaming company.
The tables in the database are account, account_date_session, and iap_purchase. 
The table account stores the details of the users, iap_purchase holds information related to in-app purchases made by users, account_date_session contains the number of sessions for the users for the days they have been active. 
•	The account table contains the attributes account_id of the user that identifies each user uniquely, created_time of the account, the created_device such as iphone4,iphone5, ipad and so on , created_platform being either ios or Android, country_code, and the created_app_store_id which uniquely identifies the app store that created the account. There are 112792 account records altogether.
•	The iap_purchase table contains the attributes account_id of the user, the account created_time, package_id_hash which uniquely identifies each package that is purchased, iap_price_usd_cents which contains the price of the package, and the app_store_id. There are 9909 packages purchased by the users.
•	The account_date_session table contains the attributes account_id of the user, date, session_count showing the number of sessions ,session_duration_sec containing session duration in seconds. There are 1698974 sessions recorded in the database for the year 2016.
Dataset covers data for the entire year of 2016. The dataset could be utilized for analyzing user behavior, understanding in-app purchasing patterns, or assessing user engagement through session data. The outcomes of data analysis could be used in customer segmentation, revenue analysis, or user engagement studies. The data is relational and stored in SQLite.

The 'avg_rev_pm_pu' code file contains the calculation of average revenue per market per user. 
The  'avg_cal' file contains the code to visualize bar chart for the average revenue per market per user.
The 'DAU_with_time' contains the code to plot time series graph for Daily Active Users with time in the year.
The 'revenue_map' contains the code for the geographical distribution of the revenue.
The 'user_map' contains the code for the geographical distribution of the users.
The 'Report' is a presentation of some analysis conducted on the dataset.
