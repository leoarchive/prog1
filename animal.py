from enum import Enum

class TipoAnimal(Enum):
    Cao=1
    Gato=2
    Passaro=3

class Animal:
    animais=[]
    __slots__=['__tipo','__especie','__nome','__dono']
    def __init__(self,tipo:TipoAnimal,especie:str,nome:str,dono:'Cliente')->None:
        self.tipo=tipo
        self.especie=especie
        self.nome=nome
        self.dono=dono
        Animal.animais.append(self)

    @property
    def tipo(self)->TipoAnimal: return self.__tipo
    @property
    def especie(self)->str: return self.__especie
    @property
    def nome(self)->str: return self.__nome
    @property
    def dono(self)->'Cliente': return self.__dono

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
    def dono(self,dono:'Cliente')->None:
        if not hasattr(self,'__dono'):
            self.__dono=None
        
        if dono.__class__.__name__ == 'Cliente':
            self.__dono=dono
        else: raise TypeError('Dono deve ser um Cliente')

    def __str__(self)->str:
        return f'Espécie: {self.especie}; Nome: {self.nome}; Dono: {self.dono.nome}.'

    def falar(self, animal:str)->str:
        return f"O {animal} faz "
    

class Cao(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
         super().__init__(TipoAnimal.Cao,especie,nome,dono)
    def falar(self)->str:
        return super().falar('Cachorro') + "AU AU!"

class Gato(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
         super().__init__(TipoAnimal.Gato,especie,nome,dono)
    def falar(self)->str:
        return super().falar('Gato') + "MIAU!"

class Passaro(Animal):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
         super().__init__(TipoAnimal.Passaro,especie,nome,dono)
    def falar(self)->str:
        return super().falar('Pássaro') + "PIU PIU!"
    
