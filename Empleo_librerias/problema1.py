import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Genera una excepción si la solicitud no fue exitosa
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def calcular_costo_en_usd(cantidad_bitcoins, precio_bitcoin_usd):
    costo_usd = cantidad_bitcoins * precio_bitcoin_usd
    return costo_usd

def main():
    try:
        cantidad_bitcoins = float(input("Por favor, introduzca la cantidad de Bitcoins que posee: "))
        precio_bitcoin_usd = obtener_precio_bitcoin()
        if precio_bitcoin_usd is not None:
            costo_usd = calcular_costo_en_usd(cantidad_bitcoins, precio_bitcoin_usd)
            print(f"El costo actual de {cantidad_bitcoins} Bitcoins es: ${costo_usd:,.4f}")
        else:
            print("No se pudo obtener el precio actual de Bitcoin.")
    except ValueError:
        print("Por favor, introduzca una cantidad válida de Bitcoins.")

if __name__ == "__main__":
    main()
