import csv
import threading
from sqlthreading import conn_pool
from sqlthreading import execute_query
from database import output_file

def main():


# use classicmodels;
# CREATE TABLE IF NOT EXISTS classicmodels.Online_Retails_Dataset (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 InvoiceNo INT,
#                 StockCode VARCHAR(50),
#                 Description TEXT,
#                 Quantity INT,
#                 InvoiceDate DATE,
#                 UnitPrice FLOAT,
#                 CustomerID INT,
#                 Country VARCHAR(100)
#             );


if __name__=="__main__":
    main()