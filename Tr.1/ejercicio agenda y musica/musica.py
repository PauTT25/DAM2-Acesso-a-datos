import os
def mostrar(carpeta, espacios):
    for nombre in sorted(os.listdir(carpeta)):
        print (espacios + nombre)
        ruta_completa = os.path.join(carpeta, nombre)
        if os.path.isdir(ruta_completa):
            mostrar(ruta_completa, espacios + "   ")

print("--- MI MUSICA ---")
os.makedirs("mi_musica/rock/clasicos", exist_ok=True)
os.makedirs("mi_musica/pop/actual", exist_ok=True)
open ("mi_musica/lista.txt", "a").close()
open("mi_musica/rock/clasicos/rock1.mp3", "a").close()
mostrar("mi_musica", "")