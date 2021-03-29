from processo import *
from frufru import *

class FilaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)


class FilaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    @property
    def inicio(self):
        if self.vazia_fila():
            raise FilaException('A fila está vazia')

        return self._inicio


    def vazia_fila(self):
        return self._tamanho == 0


    def tamanho_fila(self):
        return self._tamanho


    def inserir_fila(self, statusf, custof, descricaof, codf):
        novo = Processo(statusf, custof, descricaof, codf)

        aux = self._inicio

        if aux == None:
            self._inicio = novo

        else:
            while aux.prox != None:
                aux = aux.prox

            aux.prox = novo

        self._tamanho += 1


    def remover_fila(self):
        if self.vazia_fila():
            raise FilaException('A fila está vazia')

        self._inicio = self._inicio.prox
        self._tamanho -= 1


    def mostrar_elemento_fila(self):
        if self.vazia_fila():
            raise FilaException('A fila está vazia')

        return f'O processo que está no início da fila possui: \n  Status: {self._inicio.status}\n  Custo: R${self._inicio.custo}\n  Descrição: {self._inicio.descricao}\n  Código: {self._inicio.cod}'


    def __str__(self):
        saida = 'Fila: ['
        p = self._inicio

        while p != None:
            saida += f'(Status: {p.status} Custo: R${p.custo} Descrição: {p.descricao} Código: {c[22]}{p.cod}{c[0]})'
            p = p.prox

            if p != None:
                saida += ', '

        saida += ']'
        return saida
