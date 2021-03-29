from processo import *
from frufru import *


class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)


class ListaEncadeada:
    def __init__(self):
        self._posicao0 = None
        self._tamanho = 0


    @property
    def posicao0(self):
        if self.vazia_lista():
            raise ListaException('A lista está vazia')

        return self._posicao0


    def vazia_lista(self):
        return self._tamanho == 0


    def tamanho_lista(self):
        return self._tamanho


    def inserir_lista(self, statusl, custol, descricaol, codl, posic):
        atual = self._posicao0
        novo_no = Processo(statusl, custol, descricaol, codl)
        cont = 1

        #No começo
        if posic == 1:
           novo_no.prox = self._posicao0
           self._posicao0 = novo_no
           self._tamanho += 1
           return ''

        # Percorrendo a lista
        while (atual != None) and (cont < (posic -1)):
           atual = atual.prox
           cont += 1

        #Posição inexistente
        if atual == None:
            return ''

        #Inserindo no meio ou final
        else:
            novo_no.prox = atual.prox
            atual.prox = novo_no
            self._tamanho += 1
            return ''


    def remover_lista(self, posic):
        if self.vazia_lista():
            raise ListaException('A lista está vazia')

        # No começo
        if posic == 1:
            self._posicao0 = self._posicao0.prox
            self._tamanho -= 1
            return ''

        atual = self._posicao0
        anterior = None
        cont = 1

        while((atual != None) and (cont < posic)):
            anterior = atual
            atual = atual.prox
            cont += 1

        # posição inválida
        if atual == None:
            return f'Posição inválida'

        anterior.prox = atual.prox
        self._tamanho -= 1
        return ''


    def mostrar_elemento_lista(self, posic):
        if self.vazia_lista():
            raise ListaException('A lista está vazia')

        atual = self._posicao0
        cont = 0
        aux = None

        while ((atual != None) and (cont < posic)):
            atual = atual.prox
            cont += 1

        aux = atual

        return aux


    def ordenar(self):
        if self.vazia_lista():
            raise ListaException('A lista está vazia')

        final = None
        while final != self._posicao0:
            g = p = self._posicao0
            while p.prox != final:
                q = p.prox
                if p.cod > q.cod:
                    p.prox = q.prox
                    q.prox = p
                    if p != self._posicao0:
                        g.prox = q
                    else:
                        self._posicao0 = q
                    p, q = q, p
                g = p
                p = p.prox
            final = p


    def buscar(self, cod):
        if self.vazia_lista():
            raise ListaException('A lista está vazia')

        atuali = self._posicao0

        while atuali != None:
            if atuali.cod == cod:
                return atuali

            atuali = atuali.prox


    def __str__(self):
        saida = 'Lista: ['
        ponteirinho = self._posicao0

        while ponteirinho != None:
            saida += f'(Status: {ponteirinho.status} Custo: R${ponteirinho.custo} Descrição: {ponteirinho.descricao} Código: {c[27]}{ponteirinho.cod}{c[0]})'
            ponteirinho = ponteirinho.prox

            if ponteirinho != None:
                saida += ', '

        saida += ']'
        return saida
