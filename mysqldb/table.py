import mysql.connector
from pathlib import Path
import configparser

# Read the config.cfg file
config_file_path = Path(__file__).resolve().parent / 'config.cfg'
config = configparser.ConfigParser()
config.read(config_file_path)

# Get the database connection details from the config file
db_host = config.get('LOCAL_DATABASE', 'host')
db_user = config.get('LOCAL_DATABASE', 'user')
db_password = config.get('LOCAL_DATABASE', 'password')
db_database = config.get('LOCAL_DATABASE', 'database')

# Establish the database connection
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

cursor = db.cursor()

# Read the SQL file
sql_file_path = Path(__file__).resolve().parent / 'init_table.sql'
with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.execute(sql_script)

