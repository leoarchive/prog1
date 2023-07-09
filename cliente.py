class Cliente:
    __slots__=['__nome','__codigo','__documento','__endereco']
    def __init__(self,nome:str,codigo:int,documento:str,endereco:str)->None:
        self.nome=nome
        self.codigo=codigo
        self.documento=documento
        self.endereco=endereco

    @property
    def nome(self)->str: return self.nome
    @property
    def codigo(self)->str: return self.codigo
    @property
    def documento(self)->str: return self.documento
    @property
    def endereco(self)->str: return self.endereco

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

    @documento.setter
    def documento(self,documento:str)->None:
        if not hasattr(self,'__documento'):
            self.__documento=None
        
        if isinstance(documento,int):
            self.__documento=documento
        else: raise TypeError('Documento deve ser uma string')

    @endereco.setter
    def endereco(self,endereco:str)->None:
        if not hasattr(self,'__endereco'):
            self.__endereco=None
        
        if isinstance(endereco,int):
            self.__endereco=endereco
        else: raise TypeError('Endereco deve ser uma string')