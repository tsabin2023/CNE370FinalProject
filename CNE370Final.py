# Tyler Sabin
# CNE 370 Spring Quarter 2024
# 5/31/2024

import mysql.connector

# db connection info

config = {
    'user': 'maxuser',
    'password': 'maxpwd',
    'host': 'localhost',  # Replace with MaxScale host
    'port': 3306,         # Replace with MaxScale port
    'database': 'your_database_name'  # Update with final database name
}

# connect to Db

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

# query largest zipcode in zipcodes_one

    query = "SELECT MAX(zipcode) FROM zipcodes_one;"
    cursor.execute(query)
    print("Largest Zipcode in zipcodes_one:", cursor.fetchone()[0])

# query all zipcodes where state=KY (Kentucky)

    query = "SELECT zipcode FROM zipcodes_one WHERE state='KY';"
    cursor.execute(query)
    print("\nZipcodes in Kentucky:")
    for row in cursor.fetchall():
        print(row[0])

# query all zipcodes between 40000 and 41000

    query = "SELECT zipcode FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;"
    cursor.execute(query)
    print("\nZipcodes between 40000 and 41000:")
    for row in cursor.fetchall():
        print(row[0])

# query TotalWages column where state=PA (Pennsylvania)

    query = "SELECT TotalWages FROM your_table_name WHERE state='PA';"  # Replace your_table_name with final table name
    cursor.execute(query)
    print("\nTotalWages in Pennsylvania:")
    for row in cursor.fetchall():
        print(row[0])

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals():
        cnx.close()
