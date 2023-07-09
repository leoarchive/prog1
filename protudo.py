class Produto:
    __slots__=['__nome','__codigo']
    def __init__(self,nome:str,codigo:int)->None:
        self.nome=nome
        self.codigo=codigo

    @property
    def nome(self)->str: return self.nome
    @property
    def codigo(self)->int: return self.codigo

    @nome.setter
    def nome(self,nome:str)->None:
        if not hasattr(self,'__nome'):
            self.__nome=None
        
        if isinstance(nome,str):
            self.__nome=nome
        else: raise TypeError('Nome deve ser uma string')

    @codigo.setter
    def codigo(self,codigo:int)->None:
        if not hasattr(self,'__codigo'):
            self.__codigo=None
        
        if isinstance(codigo,int):
            self.__codigo=codigo
        else: raise TypeError('Código deve ser um inteiro')
