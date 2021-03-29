from processo import *
from frufru import *

class PilhaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)


class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    @property
    def topo(self):
        if self.vazia_pilha():
            raise PilhaException('A pilha está vazia')

        return self._topo

    def vazia_pilha(self):
        return self._tamanho == 0

    def tamanho_pilha(self):
        return self._tamanho


    def inserir_pilha(self, statusp, custop, descricaop, codp):
        no = Processo(statusp, custop, descricaop, codp)
        no.prox = self._topo
        self._topo = no

        self._tamanho += 1


    def remover_pilha(self):
        if self.vazia_pilha():
            raise PilhaException('A pilha está vazia')

        self._topo = self._topo.prox
        self._tamanho -= 1


    def mostrar_elemento_pilha(self):
        if self.vazia_pilha():
            raise PilhaException('A pilha está vazia')

        return f'O processo que está no topo da pilha possui: \n  Status: {self._topo.status}\n  Custo: R${self._topo.custo}\n  Descrição: {self._topo.descricao}\n  Código: {self._topo.cod}'


    def __str__(self):
        saida = 'Pilha: ['
        p = self._topo

        while p != None:
            saida += f'(Status: {p.status} Custo: R${p.custo} Descrição: {p.descricao} Código: {c[32]}{p.cod}{c[0]})'
            p = p.prox

            if p != None:
                saida += ', '

        saida += ']'
        return saida
