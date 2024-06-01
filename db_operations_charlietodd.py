'''Project 5 SQL
Create a Python script that demonstrates the ability to interact with a SQL database, 
including creating a database, defining a schema, and executing various SQL commands. 
Incorporate logging to document the process and provide user feedback.
'''
#Import dependencies
import pathlib
import pandas as pd
import sqlite3

#Define the database file in the project folder
db_file = pathlib.Path("datafun-05-sql", "project.db")

#Function to read data from CSV files and insert the records into tables
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

#The following function records the data from the dataframe into the SQL Script
def insert_records():
    try:
        with sqlite3.connect(db_file)as conn:
            sql_file = pathlib.Path("sql", "insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data:", e)





