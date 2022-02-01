import mysql.connector
import json

conn = mysql.connector.connect(user='root', password='Nivethaprithivi@123',
                              host='localhost',database='PythondB')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

class create_dict(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

mydict = create_dict()
select_movie = """SELECT * FROM movies"""
cursor = conn.cursor()
cursor.execute(select_movie)
result = cursor.fetchall()

for row in result:
    mydict.add(row[0],({"movie_name":row[1],"YOR":row[2],"Genres":row[3]}))

stud_json = json.dumps(mydict, indent=2, sort_keys=True)

print(stud_json)
with open("movie_data.json", "w") as p:
	json.dump(mydict, p)
