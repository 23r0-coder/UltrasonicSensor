import psycopg2

#FIX Table --------------- 'readings in database'

def sendData(distance,sound,color_led):
    """
    It connects to the database, creates a cursor, creates a SQL statement, prints a message, creates a
    tuple with the data, executes the SQL statement, prints a message, commits the data, and closes the
    connection
    
    :param distance: distance in cm
    :param sound: The sound level in decibels
    :param color_led: This is the color of the LED. It can be either "RED", "GREEN", or "BLUE"
    """
    conexion1 = psycopg2.connect(database="Distance_Readings", user="postgres", password="1234")
    cursor1=conexion1.cursor()
    sql="insert into readings(distance, sound, color_led) values (%s, %s, %s, %s)"
    print("Saving Data...")
    #Trial values
    # datos=(9.5, 3000,"RED")
    datos=(distance, sound, color_led)
    cursor1.execute(sql, datos)
    print("Data saved.")
    conexion1.commit()
    conexion1.close() 