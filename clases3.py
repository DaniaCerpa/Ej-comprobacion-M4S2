class Animal:
    """Clase representativa a animales
       Sus atributos son Nombre, Raza, Edad y Peso.
       Se establece un metodo __str__ para a traves de una cadena representar las caracteristicas del animal.
    """
    
    def __init__(self, nombre:str, raza:str, edad:int, peso:float) -> None:
       self.nombre = nombre
       self.raza = raza
       self.edad = edad
       self.peso = peso
       
    def __str__(self) -> str:
        return f"El nombre del animal es {self.nombre}, su raza es {self.raza}, su edad es de {self.edad} años, y su peso es de {self.peso} kg"


caballo = Animal("Zeus", "Pura sangre", 5, 450)
leon = Animal("Boulder", "Atlas", 10, 130)

print(caballo)
print(leon)