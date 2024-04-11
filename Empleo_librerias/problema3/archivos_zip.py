import os
import zipfile

# crear archivo zipeado
directorio = './naturaleza'
archivos = os.listdir(directorio)

with zipfile.ZipFile('naturaleza.zip', 'w') as zip:
    for file in archivos:
        archivo_path = os.path.join(directorio, file)

        if os.path.isfile(archivo_path):
            zip.write(archivo_path
                      ,  os.path.basename(archivo_path) # para evitar subcarpetas
                      )