NOMBRE_FICHERO = "catalogo_peliculas.txt"


def escribir_varias_peliculas ():
    peliculas = [
            "Matrix,148\n",
            "Titanic,195\n",
            "Avatar,162\n",
    ]
    fichero = open(NOMBRE_FICHERO, "w")
    fichero.writelines(peliculas)
    fichero.close()