import  mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("jack", "Hyd")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")