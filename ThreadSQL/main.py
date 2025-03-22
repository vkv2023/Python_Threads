import csv
import threading
from sqlthreading import conn_pool
from sqlthreading import execute_query
from database import output_file


def main():
    # SQL query to fetch a large dataset (Adjust your query as needed)
    query = "SELECT * FROM classicmodels.customers"

    # SQL query to fetch a large dataset (without LIMIT/OFFSET)
    # Get the total number of rows in the table to partition the data
    # query_count = "SELECT count(*) FROM classicmodels.customers"
    query_max = "SELECT max(customerNumber) FROM classicmodels.customers"

    # Get the total number of rows in the table to partition the data
    connection_count = conn_pool.get_connection()
    cursor = connection_count.cursor()
    # cursor.execute(query_count)
    cursor.execute(query_max)
    # returns the first element of the tuple
    total_rows = cursor.fetchone()[0]
    cursor.close()
    connection_count.close()

    # Start multiple threads to execute the query
    threads = []
    num_threads = 4  # number of threads to use
    rows_per_thread = total_rows // num_threads

    # Write headers to CSV file once (only the first thread should do this)
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # columns = [col[0] for col in cursor.description]
        # Writing headers (adjust according to your table schema)
        writer.writerow(['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6'])
        # writer.writerow(columns)

    # Start threads to execute the queries and write the results to CSV
    # threads = []
    for i in range(num_threads):
        # this will work for query_count or query_max
        start_id = i * rows_per_thread + 1
        end_id = (i + 1) * rows_per_thread + 1

        # Make sure the last thread handles any remaining rows
        if i == num_threads - 1:
            end_id = total_rows + 1
        thread = threading.Thread(target=execute_query, args=(i, query, conn_pool, output_file, start_id, end_id))
        threads.append(thread)
        print(f"{start_id}-{end_id}")
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f"Data extraction and merging completed. Results are saved to {output_file}")


if __name__ == '__main__':
    main()
