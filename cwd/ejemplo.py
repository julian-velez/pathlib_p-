from pathlib import Path
# Importamos la clase Path desde el módulo pathlib.
# pathlib es un módulo de Python que sirve para trabajar
# con rutas y archivos del sistema de una forma más sencilla.


# cwd significa "Current Working Directory"
# Es decir: "directorio de trabajo actual".


directory = Path.cwd()
# Path.cwd() obtiene la ruta de la carpeta en la que
# actualmente se está ejecutando nuestro programa.
#
# Esa ruta se convierte en un objeto Path.
#
# Por ejemplo, podría devolver:
# Windows:
# C:\Users\Julian\Documents\proyecto
#
# Linux:
# /home/julian/proyecto


print(directory)
# Imprimimos en pantalla el directorio actual.
#
# Por ejemplo, podríamos obtener:
# C:\Users\Julian\Documents\proyecto