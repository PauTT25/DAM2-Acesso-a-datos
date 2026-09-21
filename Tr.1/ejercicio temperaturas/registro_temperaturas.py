NOMBRE_FICHERO_TEMPERATURAS = "temperaturas.txt"
NOMBRE_FICHERO_CONTADOR = "contador.bin"


def escribir_temperaturas():
    print("\n--- 1. Flujo de salida: escribiendo en el fichero ---")

    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "w")
    flujo.write("18.5\n")
    flujo.write("21.0\n")
    flujo.write("19.2\n")
    flujo.close()

    print(f"Se ha escrito '{NOMBRE_FICHERO_TEMPERATURAS}' correctamente.")


def leer_temperaturas():
    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    contenido = flujo.read()
    flujo.close()

    print(contenido)


def saltar_primera_temperatura():
    print("--- 3. Moviendo el puntero con seek() ---")

    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    flujo.readline()
    posicion = flujo.tell()
    flujo.seek(0)
    flujo.seek(posicion)
    resto = flujo.read()
    flujo.close()

    print("Nos saltamos la primera línea y leemos el resto:")
    print(resto)


def comprobar_fichero_configuracion():
    print("--- 4. Manejo de excepciones ---")

    try:
        flujo = open("configuracion.txt", "r")
        flujo.close()
    except FileNotFoundError:
        print("Error controlado: el fichero no existe, pero el programa no se cae.")


def guardar_numero_registros():
    print("\n--- 5. Trabajando con un fichero binario ---")

    datos = bytes([3])

    flujo_salida = open(NOMBRE_FICHERO_CONTADOR, "wb")
    flujo_salida.write(datos)
    flujo_salida.close()

    flujo_entrada = open(NOMBRE_FICHERO_CONTADOR, "rb")
    leido = flujo_entrada.read()
    flujo_entrada.close()

    print(f"Bytes escritos:  {list(datos)}")
    print(f"Bytes leídos:    {list(leido)}")
    print(f"Como texto:      {leido.decode('utf-8')}")


def main():
    escribir_temperaturas()
    leer_temperaturas()
    saltar_primera_temperatura()
    comprobar_fichero_configuracion()
    guardar_numero_registros()


if __name__ == "__main__":
    main()