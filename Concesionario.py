class Auto:
    def __init__(self, marca, modelo, año, color, tipo_combustible, tipo_transmision, kilometraje, nacionalidad, precio_compra, tipo_vehiculo):
        # Inicialización de las características del auto
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible  # Por ejemplo, "gasolina", "diesel", "eléctrico"
        self.tipo_transmision = tipo_transmision  # Por ejemplo, "manual", "automática"
        self.kilometraje = kilometraje
        self.nacionalidad = nacionalidad  # "nacional" o "importado"
        self.precio_compra = precio_compra
        self.tipo_vehiculo = tipo_vehiculo  # "SUV", "sedán", "pickup", etc.
        
        # Características fijas por ley
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        
        # Calcular el precio de venta basado en el margen de ganancia del 40%
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        """Calcula el precio de venta del auto aplicando el margen de ganancia del 40%."""
        return self.precio_compra * 1.40

    def __str__(self):
        """Devuelve una representación en texto de todas las características del auto."""
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Año: {self.año}\n"
                f"Color: {self.color}\n"
                f"Tipo de Combustible: {self.tipo_combustible}\n"
                f"Transmisión: {self.tipo_transmision}\n"
                f"Kilometraje: {self.kilometraje} km\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Tipo de Vehículo: {self.tipo_vehiculo}\n"
                f"Ruedas: {self.ruedas}\n"
                f"Capacidad de Pasajeros: {self.capacidad_pasajeros}\n"
                f"Precio de Compra: ${self.precio_compra:.2f}\n"
                f"Precio de Venta: ${self.precio_venta:.2f}\n")

# Ejemplo de uso:

# Crear dos autos con características diferentes
auto1 = Auto("Toyota", "Corolla", 2020, "Blanco", "Gasolina", "Automática", 15000, "nacional", 20000, "sedán")
auto2 = Auto("BMW", "X5", 2022, "Negro", "Diesel", "Automática", 5000, "importado", 45000, "SUV")

# Mostrar las características de los autos
print("Características de los autos registrados en el concesionario:\n")
print(auto1)
print(auto2)
