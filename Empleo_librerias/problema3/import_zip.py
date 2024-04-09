import os
import zipfile

if not os.path.isdir('./unzip'): 
    os.mkdir('./unzip') 


# extración de archivos
with zipfile.ZipFile('naturaleza.zip', 'r') as zip_ref:
    zip_ref.extractall(path='./unzip')