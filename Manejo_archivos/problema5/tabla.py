def tabla_multiplicar(n):
    if n < 1 or n > 10:
        print("El número debe estar entre 1 y 10")
        return
    
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            resultado = n * i
            archivo.write(f"{n} x {i} = {resultado}\n")
    
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")

def mostrar_tabla(numero):
    try:
        nombre_archivo = f"tabla-{numero}.txt"
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"No existe este fichero {nombre_archivo}")

def mostrar_linea_tabla(numero, linea):
    try:
        nombre_archivo = f"tabla-{numero}.txt"
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                print(lineas[linea - 1].strip())
            else:
                print(f"No existe la línea {linea} en la tabla de multiplicar del {numero}.")
    except FileNotFoundError:
        print(f"No existe este archivo {nombre_archivo}")

def main():
    while True:
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            tabla_multiplicar(numero)
        elif opcion == '2':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla(numero)
        elif opcion == '3':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            mostrar_linea_tabla(numero, linea)
        elif opcion == '4':
            print("Un placer ayudarte, ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
