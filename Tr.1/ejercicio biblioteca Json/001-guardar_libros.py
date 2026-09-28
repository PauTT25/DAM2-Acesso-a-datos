import json

NOMBRE_FICHERO ="biblioteca.dat"

def crear_lista_libros():
    libros = [
        {"Titulo": "Cien Años de Soledad", "Autor": "Gabriel García Márquez", 
         "Año": 1967},
        {"Titulo": "Don Quijote de la Mancha", "Autor": "Miguel de Cervantes",
         "Año": 1605},
        {"Titulo": "La Sombra del Viento", "Autor": "Carlos Ruiz Zafón",
         "Año": 2001}  
    ]
    return libros

def serializar_libros(libros):
    cadena = json.dumps(libros)
    print(cadena)
    print(type(cadena))
    return cadena 

def guardar_en_fichero(cadena):
    archivo = open("biblioteca.dat","w")
    archivo.write(cadena)
    archivo.close()

if __name__ == "__main__":
    libros = crear_lista_libros()
    cadena = serializar_libros(libros)
    guardar_en_fichero(cadena)


