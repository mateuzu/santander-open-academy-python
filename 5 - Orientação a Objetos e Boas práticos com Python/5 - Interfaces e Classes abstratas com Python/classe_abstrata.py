from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self): pass

class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("Ligando TV....")
        print("TV LIGADA")

    
    def desligar(self):
        print("Desligando TV....")
        print("TV DESLIGADA")

    @property
    def marca(self):
        print("SAMSUNG")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar-condicionado....")
        print("AR-CONDICIONADO LIGADO")

    
    def desligar(self):
        print("Desligando Ar-condicionado....")
        print("AR-CONDICIONADO DESLIGADO")

    @property
    def marca(self):
        print("BRASTEMP")

controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
controle_tv.marca

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
controle_ar.marca
