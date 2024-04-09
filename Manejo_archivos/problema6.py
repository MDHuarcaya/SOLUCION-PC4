def contar_lineas_codigo(archivo):
    try:
        if not archivo.endswith('.py'):
            print("El archivo debe ser un archivo .py")
            return None

        with open(archivo, 'r') as file:
            lineas = file.readlines()
            lineas_codigo = 0
            for linea in lineas:
                linea_limpia = linea.strip()
                if linea_limpia and not linea_limpia.startswith('#'):
                    lineas_codigo += 1
            return lineas_codigo
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    cantidad_lineas = contar_lineas_codigo(ruta_archivo)
    if cantidad_lineas is not None:
        print(f"El archivo '{ruta_archivo}' tiene {cantidad_lineas} líneas de código.")

if __name__ == "__main__":
    main()
