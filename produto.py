class Produto:
    produtos=[]
    __slots__=['__nome','__codigo','__quantidade']
    def __init__(self,nome:str,codigo:int,quantidade:int=0)->None:
        self.nome=nome
        self.codigo=codigo
        self.quantidade=quantidade
        Produto.produtos.append(self)

    @property
    def nome(self)->str: return self.__nome
    @property
    def codigo(self)->int: return self.__codigo
    @property
    def quantidade(self)->int: return self.__quantidade

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

    @quantidade.setter
    def quantidade(self,quantidade:int)->None:
        if not hasattr(self,'__quantidade'):
            self.__quantidade=None
        
        if isinstance(quantidade,int):
            self.__quantidade=quantidade
        else: raise TypeError('Quantidade deve ser um inteiro')

    def __str__(self)->str:
        return f'Nome: {self.nome}; Código: {self.codigo}; Quantidade: {self.quantidade}.'

    def filtrar(**kwargs)->[str]:
        def _filtro(p):
            for key, value in kwargs.items():
                try:
                    if not getattr(p,key)==value: return False
                except:
                    raise KeyError("Chave nao encontrada na classe Produto")
            return True            
        
        return [produto for produto in Produto.produtos if _filtro(produto)]

