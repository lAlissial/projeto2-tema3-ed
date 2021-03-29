class Processo:
    def __init__(self, status, custo, descricao, cod):
        self._status = status
        self._custo = custo
        self._descricao = descricao
        self._cod = cod
        self._prox = None

    #Gets
    @property
    def status(self):
        return self._status

    @property
    def custo(self):
        return self._custo

    @property
    def descricao(self):
        return self._descricao

    @property
    def cod(self):
        return self._cod

    @property
    def prox(self):
        return self._prox

    #Sets
    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @custo.setter
    def custo(self, novo_custo):
        self._custo = novo_custo

    @descricao.setter
    def descricao(self, novo_descricao):
        self._descricao = novo_descricao

    @cod.setter
    def cod(self, novo_cod):
        self._cod = novo_cod

    @prox.setter
    def prox(self, novo):
        self._prox = novo

    #Métodos
    def incrementa_custo(self, valor):
        self._custo += valor
        return f'{self._custo}'

