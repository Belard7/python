class Cuaderno:
    def __init__(self, hojas, precio_compra): #atributos 
        self.hojas = hojas
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
        self.marca = "HOJITAS"
    
    def calcular_precio_venta(self):
        return self.precio_compra * 1.30

    def __str__(self):
        return (f"Cuaderno de {self.hojas} hojas\n"
                f"Marca: {self.marca}\n"
                f"Precio de Compra: ${self.precio_compra:.2f}\n"
                f"Precio de Venta: ${self.precio_venta:.2f}\n")


class Lapiz:
    def __init__(self, tipo, precio_compra):
        self.tipo = tipo  # "grafito" o "colores"
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
        self.marca = "RAYAS"
    
    def calcular_precio_venta(self):
        return self.precio_compra * 1.30

    def __str__(self):
        return (f"Lápiz de {self.tipo}\n"
                f"Marca: {self.marca}\n"
                f"Precio de Compra: ${self.precio_compra:.2f}\n"
                f"Precio de Venta: ${self.precio_venta:.2f}\n")


# Ejemplo de uso:

# Registrar cuadernos
cuaderno1 = Cuaderno(50, 10.00)  # Cuaderno de 50 hojas
cuaderno2 = Cuaderno(100, 15.00)  # Cuaderno de 100 hojas

# Registrar lápices
lapiz1 = Lapiz("grafito", 2.00)  # Lápiz de grafito
lapiz2 = Lapiz("colores", 3.50)  # Lápiz de colores

# Mostrar los artículos registrados
print("Artículos registrados en la papelería:\n")
print(cuaderno1)
print(cuaderno2)
print(lapiz1)
print(lapiz2)
