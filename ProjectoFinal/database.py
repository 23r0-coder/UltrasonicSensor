import psycopg2

# Connecting to the database, creating a cursor, and inserting data into the database.
conexion1 = psycopg2.connect(database="Distance_Readings", user="postgres", password="1234")
cursor1=conexion1.cursor()
sql="insert into readings(id, distance, sound, color_led) values (%s, %s, %s, %s)"
print("Guardando datos...")
#Trial values
datos=(1, 9.5, 3000,"RED")
cursor1.execute(sql, datos)
#Trial values
datos=(2, 15.3, 2500, "YELLOW")
cursor1.execute(sql, datos)
#Trial values
datos=(3, 31, 2000, "GREEN")
cursor1.execute(sql, datos)
print("Datos guardados correctamente")
conexion1.commit()
conexion1.close() 