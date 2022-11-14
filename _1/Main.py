from _1.Coche import Coche
coche1 = Coche("Renault", 5, 60, 20)
coche2 = Coche("Mercedes", 7, 90, 30)

print("Tiene", coche1.modelo,"mas autonomia que", coche2.modelo + "?")
print(coche1.mayorAutonomia(coche2))