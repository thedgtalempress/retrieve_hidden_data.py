# SQLi exploit/Retrieval of Hidden Data
This script automates the exploitation of the SQLi vulnerability in this lab: https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data. 

When the user selects a category, the application carries out a SQL query like the following:
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
