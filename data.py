import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ghada1177",
    database="mydatabase"
)
mycursor=mydb.cursor()
query="SELECT * FROM clients"
mycursor.execute(query)
records=mycursor.fetchall()
for x in records:
    print(x)