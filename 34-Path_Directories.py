from pathlib import Path

# absolute path (route of my hard disk)
# relative path (directorios dentro del proyecto)

path = Path()
# print(path.exists())          # se fija si existe el directorio
# print (path.mkdir())          # crea un directorio
# print (path.rmdir())          # borra el directorio
for file in path.glob('*'):  # path.glob es un buscador de archivos. Con loop busca en todo el directorio. '*' busca todo los archivos
    print(file)

