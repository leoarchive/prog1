from enum import Enum

class TipoAnimal(Enum):
    Cao=1
    Gato=2
    Passaro=3

class Animal:
    __slots__=['__tipo','__especie','__nome','__dono']
    def __init__(self,tipo:TipoAnimal,especie:str,nome:str,dono:'Cliente')->None:
        self.tipo=tipo
        self.especie=especie
        self.nome=nome
        self.dono=dono

    @property
    def tipo(self)->TipoAnimal: return self.tipo
    @property
    def especie(self)->str: return self.especie
    @property
    def nome(self)->str: return self.nome
    @property
    def dono(self)->'Cliente': return self.dono

    @tipo.setter
    def tipo(self,tipo:TipoAnimal)->None:
        if not hasattr(self,'__tipo'):
            self.__tipo=None
        
        if isinstance(tipo,TipoAnimal):
            self.__tipo=tipo
        else: raise TypeError('Tipo deve ser um valor válido')

    @especie.setter
    def especie(self,especie:str)->None:
        if not hasattr(self,'__especie'):
            self.__especie=None
        
        if isinstance(especie,str):
            self.__especie=especie
        else: raise TypeError('Especie deve ser uma string')

    @nome.setter
    def nome(self,nome:str)->None:
        if not hasattr(self,'__nome'):
            self.__nome=None
        
        if isinstance(nome,str):
            self.__nome=nome
        else: raise TypeError('Nome deve ser uma string')

    @dono.setter
    def dono(self,nome:'Cliente')->None:
        if not hasattr(self,'__dono'):
            self.__dono=None
        
        if nome.__class__.__name__ == 'Cliente':
            self.__dono=dono
        else: raise TypeError('Dono deve ser um Cliente')

class Cao(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
        super(TipoAnimal.Cao,especie,nome,dono)
    def acoar()->str:
        return "AU AU!"

class Gato(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
         super(TipoAnimal.Gato,especie,nome,dono)
    def miar(self)->str:
        return "MIAU!"

class Passaro(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
         super(TipoAnimal.Passaro,especie,nome,dono)
    def piar(self)->str:
        return "PIU PIU!"
    
