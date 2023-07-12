from enum import Enum

class TipoServico(Enum):
    Banho=1
    Tosa=2
    ConsultaVeterinaria=3

class Servico:
    __slots__=['__tipo']
    def __init__(self,tipo:TipoServico)->None:
        self.tipo=tipo

    @property
    def tipo(self)->TipoServico: return self.__tipo

    @tipo.setter
    def tipo(self,tipo:TipoServico)->None:
        if not hasattr(self,'__tipo'):
            self.__tipo=None
        
        if isinstance(tipo,TipoServico):
            self.__tipo=tipo
        else: raise TypeError('Tipo deve ser um valor válido')

    def __str__(self):
        if self.tipo==TipoServico.Banho: return 'Banho'
        if self.tipo==TipoServico.Tosa: return 'Tosa'
        if self.tipo==TipoServico.ConsultaVeterinaria: return 'Consulta Veterinária'

class Banho(Servico):
    def __init__(self)->None:
        super().__init__(TipoServico.Banho)

class Tosa(Servico):
    def __init__(self)->None:
        super().__init__(TipoServico.Tosa)

class ConsultaVeterinaria(Servico):
    def __init__(self)->None:
        super().__init__(TipoServico.ConsultaVeterinaria)