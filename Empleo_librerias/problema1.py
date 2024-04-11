import requests

def precio_BC():
    try:
        respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        respuesta.raise_for_status() 
        datos = respuesta.json()
        precio_USD = datos["bpi"]["USD"]["rate_float"]
        return precio_USD
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def calcular_costo_USD(cantidad_bc, precio_bc_USD):
    costo_usd = cantidad_bc * precio_bc_USD
    return costo_usd

def main():
    try:
        cantidad_bc = float(input("Por favor, introduzca la cantidad de Bitcoins que posee: "))
        precio_bc_USD = precio_BC()
        if precio_bc_USD is not None:
            costo_usd = calcular_costo_USD(cantidad_bc, precio_bc_USD)
            print(f"El costo actual de {cantidad_bc} Bitcoins es: ${costo_usd:,.4f}")
        else:
            print("No se pudo obtener el precio actual de Bitcoin.")
    except ValueError:
        print("Por favor, introduzca una cantidad válida de Bitcoins.")

if __name__ == "__main__":
    main()
