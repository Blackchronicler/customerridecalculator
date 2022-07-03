import psycopg2

hostname = "localhost"
database = "ty_psql"
username = "postgres"
pwd = "admin"
port_id = 5432


conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)



conn.close()