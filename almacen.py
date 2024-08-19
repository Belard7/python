class DispositivoElectronico:
    def __init__(self, tipo, modelo, especificaciones, color, precio_compra, fecha_lanzamiento):
        # Inicialización de las características del dispositivo
        self.tipo = tipo  # "celular", "tablet", "portátil"
        self.modelo = modelo
        self.especificaciones = especificaciones  # Especificaciones técnicas, como "8GB RAM, 128GB almacenamiento"
        self.color = color
        self.precio_compra = precio_compra
        self.fecha_lanzamiento = fecha_lanzamiento
        
        # Características fijas
        self.marca = "PHR"  # Marca fija PHR
        self.origen = "importado"  # Todos los productos son importados
        
        # Calcular el precio de venta basado en el margen de ganancia del 70%
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        """Calcula el precio de venta del dispositivo aplicando el margen de ganancia del 70%."""
        return self.precio_compra * 1.70

    def __str__(self):
        """Devuelve una representación en texto de todas las características del dispositivo."""
        return (f"Tipo: {self.tipo}\n"
                f"Modelo: {self.modelo}\n"
                f"Especificaciones: {self.especificaciones}\n"
                f"Color: {self.color}\n"
                f"Fecha de Lanzamiento: {self.fecha_lanzamiento}\n"
                f"Marca: {self.marca}\n"
                f"Origen: {self.origen}\n"
                f"Precio de Compra: ${self.precio_compra:.2f}\n"
                f"Precio de Venta: ${self.precio_venta:.2f}\n")


# Ejemplo de uso:

# Registrar dispositivos
celular = DispositivoElectronico(
    tipo="celular",
    modelo="PHR-X100",
    especificaciones="8GB RAM, 128GB almacenamiento, 6.5' pantalla",
    color="Negro",
    precio_compra=250.00,
    fecha_lanzamiento="2024-01-15"
)

tablet = DispositivoElectronico(
    tipo="tablet",
    modelo="PHR-TabA",
    especificaciones="4GB RAM, 64GB almacenamiento, 10' pantalla",
    color="Plata",
    precio_compra=300.00,
    fecha_lanzamiento="2023-11-20"
)

portatil = DispositivoElectronico(
    tipo="portátil",
    modelo="PHR-LaptopZ",
    especificaciones="16GB RAM, 512GB SSD, 15' pantalla",
    color="Gris",
    precio_compra=700.00,
    fecha_lanzamiento="2023-12-01"
)

# Mostrar los dispositivos registrados
print("Dispositivos registrados en el almacén:\n")
print(celular)
print(tablet)
print(portatil)
