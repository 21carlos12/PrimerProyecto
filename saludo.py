class Saludo():

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def saludar(self):
        print(self.mensaje)

saludo = Saludo("Hola mundo")
saludo.saludar()