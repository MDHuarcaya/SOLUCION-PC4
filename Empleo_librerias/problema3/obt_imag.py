import os
import requests

os.chdir('/workspaces/SOLUCION-PC4/naturaleza')

# url del elemento a descargar
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Bow_Lake_beim_Icefields_Parkway.jpg/640px-Bow_Lake_beim_Icefields_Parkway.jpg'

#simular que es una persona la que hace la busqueda
verificar = {'usuario': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

respuesta = requests.get(url, headers=verificar)

with open('naturaleza.jpg', 'wb') as f:
    f.write(respuesta.content)
    pass