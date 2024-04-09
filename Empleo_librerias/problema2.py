from pyfiglet import Figlet
import random

def seleccionar_fuente_aleatoria():
    figlet = Figlet()
    fuentes = figlet.getFonts()
    return random.choice(fuentes)

def imprimir_texto_con_fuente(texto, fuente):
    figlet = Figlet(font=fuente)
    texto_renderizado = figlet.renderText(texto)
    print(texto_renderizado)

def main():
    try:
        fuente = input("Por favor, ingrese el nombre de la fuente a utilizar (presione Enter para una fuente aleatoria): ").strip()
        if not fuente:
            fuente = seleccionar_fuente_aleatoria()
        texto = input("Ingrese el texto a imprimir: ")
        imprimir_texto_con_fuente(texto, fuente)
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
