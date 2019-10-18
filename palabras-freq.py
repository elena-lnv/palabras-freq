# Objetivo: este programa lee varios ficheros, dividide las líneas en palabras, calcula el porcentaje de palabras en el texto y muestra una lista.
# Abrir el fichero, leer el fichero línea por línea y dividir las líneas en lista de palabras.  
input_file_path = "sh.txt"
with open(input_file_path) as f:
    listaPalabras = [line.split() for line in f]
print(listaPalabras)
    