import csv
from mysql.connector import Error
from pydantic_core.core_schema import none_schema
from urllib3.filepost import writer
from ThreadSQLInsert.database import conn_pool


# Function to read the data from the csv file and process large result sets in chunks

def insert_data(thread_id, conn_pool, input_file, start_id, end_id, data):
    # Get a connection from the connection pool
    connection = conn_pool.get_connection()

    # Insert data into the table
    insert_query = ("INSERT INTO classicmodels.Online_Retails_Dataset (id, InvoiceNo, StockCode, Description, Quantity," 
                    " InvoiceDate, UnitPrice, CustomerID, Country) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)")

    try:

        db_info = connection.get_server_info()
        print("Server is connected..", db_info)
        cursor_ = connection.cursor()
        # Execute the SQL query with partitioning
        cursor_.execute(insert_query, data)

    except Error as err:
        print(f"Error in thread-{thread_id}: {err}")

    finally:
        if connection.is_connected():
            cursor_.close()
            connection.close()
            print("Connection is closed..")


def read_and_insert_csv(filepath):
    None


