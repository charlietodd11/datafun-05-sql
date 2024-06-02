'''Project 5 SQL
Create a Python script that demonstrates the ability to interact with a SQL database, 
including creating a database, defining a schema, and executing various SQL commands. 
Incorporate logging to document the process and provide user feedback.
'''
#Import dependencies
import pathlib
import pandas as pd
import sqlite3
import logging

#Define the database file in the project folder
db_file = pathlib.Path("project.db")

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


#Define create_database function
def create_database():
    '''Function to create a database.'''
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print('project.db successfully created.')
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql/create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

#Function to read data from CSV files and insert the records into tables
def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data/authors.csv")
        book_data_path = pathlib.Path("data/books.csv")
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
            sql_file = pathlib.Path("sql/insert_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

#The following function updates an entry in the books table
def update_records():
    with sqlite3.connect(db_file) as conn:
        sql_file = pathlib.Path('sql/update_records.sql')
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

#The following function deletes an entry in the books table
def delete_records():
    with sqlite3.connect(db_file) as conn:
        sql_file = pathlib.Path('sql/delete_records.sql')
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

#The following function calls a query of aggregated data from the books table.
def query_aggregation():
    try:
        with sqlite3.connect(db_file)as conn:
            sql_file = pathlib.Path("sql/query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            agg = cursor.fetchone()
            print("Total Books: ", agg[0])
            print("Average Year Published: ", round(agg[1]))        
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

#The following function calls a query of aggregated data from the books table.
def query_filter():
    try:
        with sqlite3.connect(db_file)as conn:
            sql_file = pathlib.Path("sql/query_filters.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            old_books = cursor.fetchall()
            print(old_books)       
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

#Define main 
def main():
    logging.info("Program started") # add this at the beginning of the main method
    insert_data_from_csv()
    create_database()
    create_tables()
    insert_records()
    update_records()
    delete_records()
    query_aggregation()
    query_filter()

    logging.info("Program ended")  # add this at the end of the main method

if __name__ == "__main__":
    main()



