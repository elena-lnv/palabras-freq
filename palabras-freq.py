# Objetivo: este programa lee varios ficheros, línea por línea, dividide las líneas en palabras, calcula el porcentaje de palabras en el texto y muestra una lista.
# Abrir el fichero y dividirlo en palabras. Aunque este programa lee línea por línea, el fichero sh-procesado.txt tiene una sola línea, con el objetivo de que haya una sola lista (pendiente de mejora). 
with open("sh-procesado.txt") as fichero:
    for linea in fichero:
        palabra = linea.split()
        print(palabra)
    