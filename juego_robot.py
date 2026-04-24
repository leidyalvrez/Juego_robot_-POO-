class Robot:
    def __init__(self, nombre, bateria, escudo):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

class RobotAtaque(Robot):
    def atacar(self, objetivo):
        print(self.nombre + " ataca a " + objetivo.nombre)
        objetivo.escudo = objetivo.escudo - 10

class RobotDefensa(Robot):
    def recargar(self):
        print(self.nombre + " recarga escudo")
        self.escudo = self.escudo + 10

r1 = RobotAtaque("A", 100, 30)
r2 = RobotDefensa("B", 100, 20)

r1.atacar(r2)
r2.recargar()

print("Escudo de B:", r2.escudo)