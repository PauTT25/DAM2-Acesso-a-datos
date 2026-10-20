#(source entorno/bin/activate )-Para activar el entorno virtual con (pip install mysql-connector-python) activado.#

import mysql.connector

libros = [
    {"titulo": "Don Quijote", "paginas": 863,
     "generos": ["novela", "aventuras", "humor"]},
    {"titulo": "Platero y yo", "paginas": 144,
     "generos": ["poesía", "infantil"]},
    {"titulo": "Marianela", "paginas": 256,
     "generos": ["novela"]}
]

muestra = libros[0]
for clave in muestra.keys():
    print(clave, type(muestra[clave]))

conn = mysql.connector.connect(
    host="localhost",
    user="desfase",
    password="desfase",
    database="desfase"
)
cursor = conn.cursor()