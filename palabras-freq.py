# Objetivo: este programa lee varios ficheros, dividide las líneas en palabras, calcula el porcentaje de palabras en el texto y muestra una lista.
# Abrir el fichero, leer todo el contenido y dividir el texto en una lista de palabras.  
input_file_path = "sh.txt"
with open(input_file_path) as f:
    listaPalabras = f.read().split()
print(listaPalabras)
    