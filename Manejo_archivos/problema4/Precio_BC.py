import requests
from datetime import datetime
import pytz

def obtener_precio_bc():
    try:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        respuesta = requests.get(url)
        respuesta.raise_for_status()  
        data = respuesta.json()
        precio = {
            'USD': data['bpi']['USD']['rate'],
            'GBP': data['bpi']['GBP']['rate'],
            'EUR': data['bpi']['EUR']['rate']
        }
        return precio
    except requests.exceptions.RequestException as e:
        print("Error al obtener precio de Bitcoin:", e)
        return None
    except KeyError as e:
        print("Error al analizar los datos de la API:", e)
        return None

def obtener_tiempo_peru():
    peru = pytz.timezone('America/Lima')
    fecha_hora_peru = datetime.now(peru)
    return fecha_hora_peru.strftime("%Y-%m-%d %H:%M:%S %Z")

def guardar_precio(precio, archivo):
    try:
        with open(archivo, 'a') as file:
            fecha_hora = obtener_tiempo_peru()
            file.write("Fecha y hora: {}\n".format(fecha_hora))
            file.write("Precio de Bitcoin:\n")
            for moneda, precio in precio.items():
                file.write(f"{moneda}: {precio}\n")
            file.write('\n')
        print("Precios de Bitcoin guardados en el archivo:", archivo)
    except IOError as e:
        print("Error al guardar los precios en el archivo:", e)

# Obtener los precios de Bitcoin
precio_bitcoin = obtener_precio_bc()
if precio_bitcoin:
    print("Precios de Bitcoin en USD, GBP y EUR:")
    for moneda, precio in precio_bitcoin.items():
        print(f"{moneda}: {precio}")
    
    # Guardar los precios en un archivo
    archivo = 'precio_bitcoin.txt'
    guardar_precio(precio_bitcoin, archivo)

