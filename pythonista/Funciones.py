def hola(nombre="Mundo"):
    print("Hola ", nombre)

hola("Michelle")
hola()

class Animal:
    def __init__(self, patas=4, tipo="pequeño"):
        self.patas = patas
        self.tipo = tipo

class Perro(Animal):
    def __init__(self, nombre="Oddy", raza="jack"):
        self.nombre = nombre
        self.raza = raza
        super.
    #def saludo(self):
    #    return  "Te saluda %s" % self.nombre

perrito = Perro(nombre="Bobby ", raza="Golden ")
perrito_juan = Perro()
print(perrito.nombre)
print(perrito.raza)
#print(perrito.patas)
#print(perrito.tipo)
#perrito.saludo()
print(perrito_juan.nombre)
print(perrito_juan.raza)
#perrito_juan.saludo()



