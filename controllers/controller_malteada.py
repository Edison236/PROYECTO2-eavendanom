def calcular_costo(self) -> float:
        return sum(ingrediente.precio for ingrediente in self.ingredientes) + 500
    
def calcular_calorias(self):
    return sum(ingrediente.calorias for ingrediente in self.ingredientes) + 200

def calcular_rentabilidad(self):
    costo = self.calcular_costo()
    return (self.precio_publico - costo) / costo if costo > 0 else 0