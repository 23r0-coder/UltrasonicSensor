import mysql.connector

# Defining the variables that will be used to connect to the database.
DB_USER 	= "admin"
PASSWORD 	= "admin123"
DB_SERVER 	= ""
DB_NAME 	= "DistanceReads"


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