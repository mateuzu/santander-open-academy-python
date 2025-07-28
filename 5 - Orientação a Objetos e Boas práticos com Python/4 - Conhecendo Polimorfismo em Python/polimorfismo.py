class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self): 
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self): 
        print("Avestruz não voa")

# FIXME: exemplo ruim do uso de herança para utilizar o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião voando...")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal()) # Pardal voa
plano_de_voo(Avestruz()) # Avestruz não voa