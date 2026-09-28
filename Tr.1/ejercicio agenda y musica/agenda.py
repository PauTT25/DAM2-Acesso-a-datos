class Agenda:    
    def __init__(self, archivo): 
        self.archivo = archivo 
 
    def guardar(self, nombre, telefono): 
        f = open(self.archivo, "a") 
        f.write(nombre + "," + telefono + "\n") 
        f.close() 
 
    def leer(self): 
        f = open(self.archivo, "r") 
        for linea in f: 
            datos = linea.strip().split(",") 
            print("Nombre: " + datos[0] + " Telefono: " + datos[1]) 
        f.close()


print("--- MI AGENDA ---") 
agenda = Agenda("Agenda.csv") 
agenda.guardar("Juan", "123456789") 
agenda.guardar("Maria", "987654321") 
agenda.leer()