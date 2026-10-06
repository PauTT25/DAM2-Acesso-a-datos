libros = [
    {"titulo": "Don Quijote", "paginas": 863,
     "generos": ["novela", "aventuras", "humor"]},
    {"titulo": "Platero y yo", "paginas": 144,
     "generos": ["poesía", "infantil"]},
    {"titulo": "Marianela", "paginas": 256,
     "generos": ["novela"]}
]

pip install mysql-connector-python

import mysql.connector 
mysql.connector.conect(host="localhost", user="root", password="", database="mascotas_db")