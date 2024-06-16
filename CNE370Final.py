# Tyler Sabin
# sabint@live.com
# 6/15/2024
# CNE 370 Spring Quarter 2024
# This code queries shard architecture on a VM server and returns results to terminal
# source Matt Bennett
# source https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
# source https://stackoverflow.com/questions/13076194/ascii-art-in-python
# code modified by Tyler Sabin


import mysql.connector

# uses ANSI escape codes for bold text
BOLD = '\033[1m'
RESET = '\033[0m'

# db connection to VM server info

def connect_to_db():
    return mysql.connector.connect(
        user='maxuser',
        password='maxpwd',
        host='10.0.0.228',  # replace '10.0.0.28'  with your server's ip address, eg. '10.0.0.9'
        port='4000',
    )

# define row result function
def row_result(result):
    for row in result:
        print(row)

# defining execute query
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()  # fetches all rows of a query and returns result
    cursor.close()
    return result

# function to print query header with ASCII art
def print_header(header_text):
    print("*" * (len(header_text) + 4))
    print(f"* {BOLD}{header_text}{RESET} *")
    print("*" * (len(header_text) + 4))

# function to turn vertical results into horizontal results
def hor_results(connection, queries, all_zipcodes):
    try:
        # execute each query with results
        for query in queries:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            all_zipcodes.extend(result)
            cursor.close()  # close the cursor after results

        # display 15 results per line
        results_per_line = 15
        num_results = len(all_zipcodes)
        for i in range(0, num_results, results_per_line):
            # join 15 zipcodes with space
            line = ' '.join([str(row[0]) for row in all_zipcodes[i:i + results_per_line]])
            print(line)

    finally:
        # close cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

# define query 1
# the largest zipcode in zipcodes_one
def query_1(connection):
    print()
    print_header("1. The largest zipcode in zipcodes_one:")
    print()
    query = "SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY zipcode DESC LIMIT 1;"
    result = execute_query(connection, query)
    row_result(result)

# define query 2
# all zipcodes where state=KY (Kentucky)
def query_2(connection):
    print()
    print_header("2. All zipcodes where state=KY (Kentucky):")
    print()

    queries = [
        "SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY';",
        "SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY';"
    ]

    all_zipcodes = []

    hor_results(connection, queries, all_zipcodes)

# define query 3
# all zipcodes between 40000 and 41000
def query_3(connection):
    print()
    print_header("3. All zipcodes between 40000 and 41000:")
    print()

    queries = [
        "SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode > 40000 AND Zipcode < 41000;",
        "SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE Zipcode > 40000 AND Zipcode < 41000;"
    ]

    all_zipcodes = []

    hor_results(connection, queries, all_zipcodes)

# define query 4
# the TotalWages column where state=PA (Pennsylvania)
def query_4(connection):
    print()
    print_header("4. The TotalWages column where state=PA (Pennsylvania):")
    print()

    queries = [
        "SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA';",
        "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA';"
    ]

    all_zipcodes = []

    hor_results(connection, queries, all_zipcodes)

# define connection as a global variable
connection = None

# defining main function
def main():
    # declare connection as global
    global connection
    # connect to the database
    connection = connect_to_db()

    # call query functions
    query_1(connection)
    query_2(connection)
    query_3(connection)
    query_4(connection)

    # close the database connection
    connection.close()

if __name__ == "__main__":
    main()
    
