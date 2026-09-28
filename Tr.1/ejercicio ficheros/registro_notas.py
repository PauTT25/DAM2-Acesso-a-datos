import os

def guardar_notas():
    notas = [("Lucia", "Matematicas", "8.5"), ("Marcos", "Matematicas", "6.0"), ("Sofia", "Lengua", "9.0")]
    with open("notas.csv", "a") as archivo:
        for nota in notas:
            linea = ",".join(nota) + "\n"
            archivo.write(linea)

def leer_notas():
    notas_leidas = []
    with open("notas.csv", "r") as archivo:
        for linea in archivo:
            tupla = tuple(linea.strip().split(","))
            notas_leidas.append(tupla)
    print(notas_leidas)
    return notas_leidas


                
    
    
    