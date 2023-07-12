from datetime import date 
from enum import Enum

class TipoStatusAgendamento(Enum):
    Agendado=1
    SendoExecutado=2
    Finalizado=3


class Agendamento:
    agendamentos=[]
    __slots__=['__dataInicio','__animal','__cliente','__servico','__status']
    def __init__(self,cliente:'Cliente',animal:'Animal',servico:'Servico',dataInicio:date)->None:
        self.cliente=cliente
        self.animal=animal
        self.servico=servico
        self.servico=servico
        self.dataInicio=dataInicio
        self.status=TipoStatusAgendamento.Agendado
        Agendamento.agendamentos.append(self)

    @property
    def cliente(self)->'Cliente': return self.__cliente
    @property
    def animal(self)->'Animal': return self.__animal
    @property
    def dataInicio(self)->date: return self.__dataInicio
    @property
    def servico(self)->date: return self.__servico
    @property
    def status(self)->TipoStatusAgendamento: return self.__status

    @cliente.setter
    def cliente(self,cliente:'Cliente')->None:
        if not hasattr(self,'__cliente'):
            self.__cliente=None
        
        if cliente.__class__.__name__ == 'Cliente':
            self.__cliente=cliente
        else: raise TypeError('Cliente deve ser um Cliente válido')

    @animal.setter
    def animal(self,animal:'Animal')->None:
        if not hasattr(self,'__animal'):
            self.__animal=None
    
        if animal.__class__.__bases__[0].__name__ == 'Animal':
            self.__animal=animal
        else: raise TypeError('Animal deve ser um Animal válido')

    @dataInicio.setter
    def dataInicio(self,dataInicio:date)->None:
        if not hasattr(self,'__dataInicio'):
            self.__dataInicio=None
        
        if isinstance(dataInicio,date):
            self.__dataInicio=dataInicio
        else: raise TypeError('Data de Início deve ser uma data')

    @servico.setter
    def servico(self,servico:'Servico')->None:
        if not hasattr(self,'__servico'):
            self.__servico=None
        
        if servico.__class__.__bases__[0].__name__ == 'Servico':
            self.__servico=servico
        else: raise TypeError('Serviço deve ser um Servico válido')

    @status.setter
    def status(self,status:TipoStatusAgendamento)->None:
        if not hasattr(self,'__status'):
            self.__status=None
        
        if isinstance(status,TipoStatusAgendamento):
            self.__status=status
        else: raise TypeError('Status deve ser do tipo TipoStatusAgendamento')

    def __str__(self)->str:
        return f'Cliente: {self.cliente.nome}; Animal: {self.animal.nome}; Serviço: {self.servico}; Data: {self.dataInicio}.'

    def __del__(self)->None:
        self.status=TipoStatusAgendamento.Finalizado

    def executar(self)->None:
        self.status=TipoStatusAgendamento.SendoExecutado
