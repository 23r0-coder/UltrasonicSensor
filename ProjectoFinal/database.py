import mysql.connector

# Defining the variables that will be used to connect to the database.
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="",
  database="Distance_readings"
)


def connect(self):
    """
    It tries to connect to the database, and if it fails, it prints the error message
    """
    try:
        self.cnx = mysql.connector.connect(user=DB_USER, 
        password=PASSWORD, 
        host=DB_SERVER, 
        database=DB_NAME)
    except mysql.connector.Error as err:
        print("Failed to connect")
        print(err)

mycursor = mydb.cursor()

sql = "INSERT INTO  (distance, sound, led) VALUES (%s, %s, %s)"
val = ("15", "2000","Yellow")
mycursor.execute(sql, val)

mydb.commit()

#display the information inserted.
print(mycursor.rowcount, "record inserted.")
