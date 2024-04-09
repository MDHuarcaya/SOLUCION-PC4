import requests
from datetime import datetime
import pytz

def obtener_precios_bitcoin():
    try:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de error de solicitud HTTP
        data = response.json()
        precios = {
            'USD': data['bpi']['USD']['rate'],
            'GBP': data['bpi']['GBP']['rate'],
            'EUR': data['bpi']['EUR']['rate']
        }
        return precios
    except requests.exceptions.RequestException as e:
        print("Error al obtener los precios de Bitcoin:", e)
        return None
    except KeyError as e:
        print("Error al analizar los datos de la API:", e)
        return None

def obtener_fecha_hora_peru():
    peru = pytz.timezone('America/Lima')
    fecha_hora_peru = datetime.now(peru)
    return fecha_hora_peru.strftime("%Y-%m-%d %H:%M:%S %Z")

def guardar_precios_en_archivo(precios, archivo):
    try:
        with open(archivo, 'a') as file:
            fecha_hora = obtener_fecha_hora_peru()
            file.write("Fecha y hora: {}\n".format(fecha_hora))
            file.write("Precio de Bitcoin:\n")
            for moneda, precio in precios.items():
                file.write(f"{moneda}: {precio}\n")
            file.write('\n')
        print("Precios de Bitcoin guardados en el archivo:", archivo)
    except IOError as e:
        print("Error al guardar los precios en el archivo:", e)

# Obtener los precios de Bitcoin
precios_bitcoin = obtener_precios_bitcoin()
if precios_bitcoin:
    print("Precios de Bitcoin en USD, GBP y EUR:")
    for moneda, precio in precios_bitcoin.items():
        print(f"{moneda}: {precio}")
    
    # Guardar los precios en un archivo
    archivo = 'precios_bitcoin.txt'
    guardar_precios_en_archivo(precios_bitcoin, archivo)

