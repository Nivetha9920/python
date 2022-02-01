import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Nivethaprithivi@123",
	database = "PythondB"
)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE movie (movie_name VARCHAR(255),YOR VARCHAR(255),Genre VARCHAR(255),Awards_won VARCHAR(255),Lead_actor VARCHAR(255),Lead_actress VARCHAR(255))")
cursor.execute("SHOW TABLES")
for x in cursor:
  print(x)
