import pandas as pd

import numpy as np

import mysql.connector

host = input("Enter host (e.g., localhost): ")
user = input("Enter username: ")
password = input("Enter password: ")
database = input("Enter database name: ")

try:
    # The mysql.connector.connect() function attempts to create a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,       # MySQL server hostname or IP address
        user=user,       # MySQL username
        password=password,   # MySQL password
        database=database    # The specific database to connect to
    )

    # Checking if the connection is successful
    if connection.is_connected():
        # If connection is successful, print a success message
        print("Successfully connected to the database")

        # Creating a cursor object to execute SQL queries
        # The cursor allows us to execute queries and retrieve results
        cursor = connection.cursor()

        # Running a simple SQL query to check which database is currently being used
        cursor.execute("SELECT DATABASE();")

        # Fetching the result of the executed query
        record = cursor.fetchone()  # This fetches one row from the result set (in this case, the database name)
        print(f"You're connected to database: {record}")

        # Example: Fetch all rows from a user-specified table
        # Asking the user to input the name of the table they want to query
        table = input("Enter your table name here: ")

        # Constructing the SQL query to select all data from the given table
        query = "SELECT * FROM " + table  # SELECT * is used to fetch all columns from the table
        cursor.execute(query)  # Executing the query

        # Fetching all the rows from the executed query
        rows = cursor.fetchall()  # fetchall() retrieves all the rows returned by the query

        # Looping through the fetched data and printing each row
        for row in rows:
            print(row)

# Handling any errors that may occur during the connection or execution process
except mysql.connector.Error as e:
    # Printing an error message if the connection or query fails
    print(f"Error while connecting to MySQL: {e}")
    