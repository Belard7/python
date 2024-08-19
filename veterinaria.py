class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, telefono): # inicializa los atributos del perro
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.telefono = telefono
        self.estado = "NO ATENDIDO"
        self.tamaño = self.clasificar_tamaño()
    
    def clasificar_tamaño(self): # determina si el perro es grande o pequeño 
        if self.peso < 10:
            return "Pequeño"
        else:
            return "Grande"

    def registrar(self):
        self.estado = "ATENDIDO"
        print(f"Registro completado para {self.nombre}.")
        print(self)

    def __str__(self): #representación en texto del objeto perro 
        return (f"Nombre: {self.nombre}\n"
                f"Raza: {self.raza}\n"
                f"Edad: {self.edad} años\n"
                f"Peso: {self.peso} kg\n"
                f"Color: {self.color}\n"
                f"Dueño: {self.dueño}\n"
                f"Teléfono: {self.telefono}\n"
                f"Tamaño: {self.tamaño}\n"
                f"Estado: {self.estado}")

# Ejemplo de uso:
nombre = "Firulais"
raza = "Labrador"
edad = 3
peso = 12.5
color = "Amarillo"
dueño = "Juan Perez"
telefono = "123456789"

# Crear un objeto Perro con la información proporcionada
perro = Perro(nombre, raza, edad, peso, color, dueño, telefono)

# Registrar al perro, cambiando su estado a "ATENDIDO"
perro.registrar()
