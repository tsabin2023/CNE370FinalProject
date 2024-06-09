# Tyler Sabin
# sabint@live.com
# 6/8/2024
# CNE 370 Spring Quarter 2024
# This code queries shard architecture on a VM server and returns results to terminal
# source Christine Sutton
# source https://rtc.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=9c492e9a-b3d1-46be-a657-b1870016c05a&autoplay=False&interactivity=all&start=0&showtitle=True&offerviewer=True&captions=False&showbrand=True&ltiCourseID=Canvas%5c2471314&isLTIEmbed=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzE3NzA0NzQ5LCJuYmYiOjE3MTc3MDQ2ODksImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjoidmlld0VtYmVkZGVkQ29udGVudCIsInN1YiI6IjFkNzcxZDVmLTk3NmUtNGQxNi1hODQ3LWIwMzYwMTg3MWViOSIsImF1dGhfdGltZSI6MTcxNzcwNDY4OSwiaWRwIjoiaWRzcnYiLCJyb2xlIjoidmlld2VyIiwic2Vzc2lvbl9pZCI6IjAyNWQxYTgwLTMxNmQtNGM2My05ZWUyLWIxODcwMTRjYmVmOCIsIm5hbWUiOiJUeWxlciBTYWJpbiIsImFtciI6WyJwYXNzd29yZCJdfQ.WYxgpGloOELWWtW1i_YdYv1R4VAyM1gNNU2_QYXRY-En8ODLQZH76vl_GBaPMBmmLWLyj7ND7RYLZKIZG-uRYsOrMS8OMVgh9zqxN_maZE_KdZpEzgdvBH5tM_NLv17EMzDKWHzGcj1lKrTtYmR1NitumC6Lehub1Bfda5-SwTNHZNT8T0mJGNat5-2W85o1IBLC-uRm5URhYoIET1uI7B0QdEL6wpl4XJ2MlQbUEzJTQiGSQ8pGuWZEXQt6VNbTs-rsbVQhVFSOMa4Slyukr1FvuDOeVrXfAJuGb9B6INpcSpvK30quVbKD0GBtpEiNGDTLvBwOiZRwAquOnE651A#access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzE3NzA4Mjg5LCJuYmYiOjE3MTc3MDQ2ODksImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidmlld0VtYmVkZGVkQ29udGVudCJdLCJzdWIiOiIxZDc3MWQ1Zi05NzZlLTRkMTYtYTg0Ny1iMDM2MDE4NzFlYjkiLCJhdXRoX3RpbWUiOjE3MTc3MDQ2ODksImlkcCI6Imlkc3J2Iiwicm9sZSI6InZpZXdlciIsInNlc3Npb25faWQiOiIwMjVkMWE4MC0zMTZkLTRjNjMtOWVlMi1iMTg3MDE0Y2JlZjgiLCJuYW1lIjoiVHlsZXIgU2FiaW4iLCJhbXIiOlsicGFzc3dvcmQiXX0.TpABFkJuLLlzFYbIt7KA-oWO5-3DfnytrX0mYPbQxFNMoh56OAGk3grddJtmdg9RJAYHbyd2sa9NOODON8ij7uQTdHe_hb2EVIzxAUlSpQX8M9CgqkrHaxp1NTTDYLKoTv0ZwO7_1pUONsFppy8BI6mO89ZbD2_OAi59518KpTypvlW-aaWNAVPDGbKeKrQVayI2Es-gacDl1jJJFZScP4wqShITZoGzUFel3eBv0faEiWbXAH9-8A8ccHhMuu-yrYdrTPGAankUTwTFaiFVoDPr6K_1zTffMhkhWBmMC8HyBFrF-2BeunUuIaTENA1n2VNUCcWVK9az2QNpxhqT_w
# source Brian Huang
# source Matt Bennett
# code modified by Tyler Sabin


import mysql.connector

# db connection info
def connect_to_db():
    return mysql.connector.connect(
        user='maxuser',
        password='maxpwd',
        host='10.0.0.228',
        port='4000',
    )

# defining queries

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()  # Fetch all rows of a query result
    cursor.close()
    return result

def query_1(connection):
    print("This is query 1.")
    query = "SELECT * FROM zipcodes_one.zipcodes_one ORDER BY zipcode DESC LIMIT 1;"
    result = execute_query(connection, query)
    for row in result:
        print(row)

def query_2(connection):
    print("This is query 2.")
    queries = [
        "SELECT * FROM zipcodes_one.zipcodes_one WHERE State = 'KY';",
        "SELECT * FROM zipcodes_two.zipcodes_two WHERE State = 'KY';"
    ]

    for query in queries:
        result = execute_query(connection, query)
        for row in result:
            print(row)

def query_3(connection):
    print("This is query 3.")
    queries = [
        "SELECT * FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;",
        "SELECT * FROM zipcodes_two.zipcodes_two WHERE Zipcode BETWEEN 40000 AND 41000;"
    ]

    for query in queries:
        result = execute_query(connection, query)
        for row in result:
            print(row)

def query_4(connection):
    print("This is query 4.")
    queries = [
        "SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA';",
        "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA';"

    ]

    for query in queries:
        result = execute_query(connection, query)
        for row in result:
            print(row)


# Define other query functions similarly

connection = None  # Define connection as a global variable

def main():
    global connection  # Declare connection as global
    # Connect to the database
    connection = connect_to_db()

    # Call query functions
    query_1(connection)
    query_2(connection)
    query_3(connection)
    query_4(connection)
    # Call other query functions similarly

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
