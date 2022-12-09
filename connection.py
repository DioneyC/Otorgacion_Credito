import psycopg2
import pandas.io.sql as sqlio

connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="localhost",
                                    port="5432",
                                    dbname="credito")
cursor = connection.cursor()
sql = 'SELECT IDU, RFC, APROBADO FROM ESTATUS'
data = sqlio.read_sql_query(sql, connection)

last = len(data)
ultimo = data.tail(1)

ID = int(ultimo["idu"].values)
RFC = ultimo["rfc"].values
ESTATUS = ultimo["aprobado"].values

#print(ID)
#print(RFC[0])
#print(ESTATUS[0])

dat = {"ID":ID, "RFC":RFC[0], "ESTATUS":ESTATUS[0]}
print(dat)

connection.close()