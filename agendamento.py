from datetime import Date 
from enum import Enum

class Agendamento:
    __slots__=['__data','__animal']
    def __init__(self,data:Date,animal:'Animal')->None:
        self.data=data
        self.animal=animal

    @property
    def data(self)->Date: return self.data
    @property
    def animal(self)->'Animal': return self.animal

    @data.setter
    def data(self,data:Date)->None:
        if not hasattr(self,'__data'):
            self.__data=None
        
        if isinstance(data,Date):
            self.__data=data
        else: raise TypeError('Nome deve ser uma data')

    @animal.setter
    def animal(self,animal:'Animal')->None:
        if not hasattr(self,'__animal'):
            self.__animal=None
        
        if animal.__class__.__name__ == 'Animal':
            self.__animal=animal
        else: raise TypeError('Animal deve ser um Animal válido')

class Servico(Agendamento):
    def __init__(self,especie:str,nome:str,dono:'Cliente')->None:
        super(TipoAnimal.Cao,especie,nome,dono)
    def acoar()->str:
        return "AU AU!"