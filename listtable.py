import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ghada1177"
)
mycursor=mydb.cursor()

mycursor.execute("SELECT* FROM clients")
result = mycursor.fetchall()
for row in result:
    print(row)
    print("\n")