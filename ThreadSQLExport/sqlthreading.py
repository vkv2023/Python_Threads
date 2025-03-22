import threading
from mysql.connector import Error
import csv
from urllib3.filepost import writer
from ThreadSQLExport.database import conn_pool


# Function to execute SQL query in a separate thread and process large result sets in chunks
def execute_query(thread_id, query, conn_pool, output_file, start_id, end_id):
    # Get a connection from the connection pool
    connection = conn_pool.get_connection()

    # Update the query to include LIMIT and OFFSET or WHERE clause to partition the data
    query_with_range = f"{query} WHERE customerNumber >= {start_id} AND customerNumber < {end_id}"

    try:

        db_info = connection.get_server_info()
        print("Server is connected..", db_info)
        cursor_ = connection.cursor()
        # Execute the SQL query with partitioning
        cursor_.execute(query_with_range)

        # Open the CSV file and prepare to write the results
        # Lock file access to avoid multiple threads writing at the same time
        with threading.Lock():
            with open(output_file, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)

                # Fetch the result set in chunks to avoid loading the entire result in memory
                while True:
                    resultset = cursor_.fetchmany(1000)
                    if not resultset:
                        break
                    else:
                        results = resultset

                    # Fetch the result set in chunks to avoid loading the entire result in memory
                    print(f"thread_id-{thread_id} fetched {len(results)} rows")

                    # Write rows to the CSV file
                    writer.writerows(resultset)
                    # Example processing: Just print the first 5 rows
                    for row in results[:5]:
                        print(f"thread_id-{thread_id} row: {row}")

    except Error as err:
        print(f"Error in thread-{thread_id}: {err}")

    finally:
        if connection.is_connected():
            cursor_.close()
            connection.close()
            print("Connection is closed..")
