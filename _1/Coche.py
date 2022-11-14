class Coche:
    def __init__(self, modelo, pasajeros, deposito, kpl):
        self.modelo = modelo
        self.pasajeros = pasajeros
        self.deposito = deposito
        self.kpl = kpl
        
    def calcularAutonomia(self):
        return self.deposito * self.kpl
    
    def mayorAutonomia(self, coche): 
        return self.calcularAutonomia() > coche.calcularAutonomia()
