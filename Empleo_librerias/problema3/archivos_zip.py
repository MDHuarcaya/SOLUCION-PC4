import os
import zipfile

# creando un archivo zipeado
directory = './naturaleza'
files = os.listdir(directory)

with zipfile.ZipFile('naturaleza.zip', 'w') as zip:
    for file in files:
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            zip.write(file_path
                      ,  os.path.basename(file_path) # para evitar subcarpetas
                      )