import requests
import sqlite3
import time

# URL del API de SUNAT
url_base = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Creaando la base de datos SQLite
conexion = sqlite3.connect('dolar2023.db')
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                    fecha TEXT PRIMARY KEY,
                    compra REAL,
                    venta REAL
                  )''')

#  todos los meses del año 2023
for month in range(1, 13):
    url = f"{url_base}?month={month}&year=2023"

    try:
        # Realizar la solicitud GET al API de SUNAT
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # Obtener los datos JSON de la respuesta
            data = respuesta.json()

            # Insertar los datos en la base de datos
            for registro in data:
                fecha = registro['fecha']
                compra = registro['compra']
                venta = registro['venta']
                
                cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, compra, venta)
                                  VALUES (?, ?, ?)''', (fecha, compra, venta))
                
            # Confirmar los cambios
            conexion.commit()

        else:
            print(f"Error al obtener datos para el mes {month}: {respuesta.status_code}")

    except Exception as e:
        print(f"Error en la solicitud para el mes {month}: {str(e)}")

    # para no exceder el límite de solicitud del servidor
    time.sleep(1)

# Cerrar la conexión con la base de datos
conexion.close()

# Mostrar el contenido de la tabla
conexion = sqlite3.connect('dolar2023.db')
cursor = conexion.cursor()

# Consulta SQL para obtener el contenido de la tabla
cursor.execute('''SELECT * FROM sunat_info''')

# Mostrar el contenido de la tabla
for row in cursor.fetchall():
    print(row)

# Cerrar la conexión
conexion.close()
