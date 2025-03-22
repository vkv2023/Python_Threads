# import sqlalchemy as _sql
# import sqlalchemy.ext.declarative as _declarative
# import sqlalchemy.orm as _orm
import mysql.connector.pooling
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
MYSQL_host = os.environ.get("MYSQL_HOST")
MYSQL_db = os.environ.get("MYSQL_DB")
MYSQL_user = os.environ.get("MYSQL_USER")
MYSQL_password = os.environ.get("MYSQL_PASSWORD")
MYSQL_port = os.environ.get("MYSQL_PORT")
MYSQL_poolname = os.environ.get("MYSQL_POOLNAME")
# Number of connections in the pool
MYSQL_poolsize = os.environ.get("MYSQL_POOLSIZE")
# The CSV file to write data
output_file = "C:\\Vinod\Code\\Data\\merged_results.csv"

# Assuming your MYSQL server is running locally with a database named 'mydatabase'
# DATABASE_URL = f"{MYSQL_host},{MYSQL_db},{MYSQL_PORT},{MYSQL_user},{MYSQL_password}"

# Set up connection pool (You can adjust min, max pool size based on your requirements)
conn_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name=MYSQL_poolname, pool_size=int(MYSQL_poolsize),
    host=MYSQL_host, database=MYSQL_db,
    user=MYSQL_user, password=MYSQL_password,
    port=MYSQL_port)

# engine = _conn.create_engine(DATABASE_URL)
# SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = _declarative.declarative_base()
