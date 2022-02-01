import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Nivethaprithivi@123",
	database = "PythondB"
)

mycursor = mydb.cursor()
cursor.execute("CREATE TABLE movies (movie_name VARCHAR(255),YOR VARCHAR(255),Genre VARCHAR(255),Awards_won VARCHAR(255),Lead_actor VARCHAR(255),Lead_actress VARCHAR(255))")
sql = "INSERT INTO movies (movie_name,YOR,Genre,Awards_won,Lead_actor,Lead_actress) VALUES (%s, %s, %s, %s ,%s, %s)"
val = [('ABC', '2005', 'Thriller', '5', 'XYZ', 'DEF'),('ABCd', '2009', 'Comedy', '10', 'STU', 'VWX')]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
