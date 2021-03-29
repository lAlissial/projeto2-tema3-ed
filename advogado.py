from processo import *
from lista import *
from pilha import *
from fila import *
from frufru import *


class Advogado:
    def __init__(self, cod_oab):
        self._cod_oab = cod_oab
        self._processosL = ListaEncadeada()
        self._processosP = PilhaEncadeada()
        self._processosF = FilaEncadeada()

    #Gets
    @property
    def cod_oab(self):
        return self._cod_oab

    @property
    def processosL(self):
        return self._processosL

    @property
    def processosP(self):
        return self._processosP

    @property
    def processosF(self):
        return self._processosF

    #Sets
    @cod_oab.setter
    def cod_oab(self, novo_cod_oab):
        self._cod_oab = novo_cod_oab
    
    # Métodos

    def maior_custo(self):
        if self._processosL.vazia_lista():
            raise ListaException('A lista está vazia')

        maior = self._processosL.mostrar_elemento_lista(0)

        for i in range(self._processosL.tamanho_lista()):
            elementodavez = self._processosL.mostrar_elemento_lista(i)
            if elementodavez.custo > maior.custo:
                maior = elementodavez

        return maior


    def menor_custo(self):
        if self._processosL.vazia_lista():
            raise ListaException('A lista está vazia')

        menor = self._processosL.mostrar_elemento_lista(0)

        for i in range(self._processosL.tamanho_lista()):
            elementodavez = self._processosL.mostrar_elemento_lista(i)
            if elementodavez.custo < menor.custo:
                menor = elementodavez

        return menor


    def incrementa_custo_processo_l(self, cod, valor):
        if self._processosL.vazia_lista():
            raise ListaException('A lista está vazia')

        atual_tal = self._processosL.posicao0

        while atual_tal != None:
            if atual_tal.cod == cod:
                atual_tal.incrementa_custo(valor)
            atual_tal = atual_tal.prox

        return ''


    def adicionar_processo_P(self, statusp, custop, descricaop, codp):
        return self._processosP.inserir_pilha(statusp, custop, descricaop, codp)


    def adicionar_processo_L(self, statusl, custol, descricaol, codl, posicao):
        return self._processosL.inserir_lista(statusl, custol, descricaol, codl, posicao)


    def adicionar_processo_F(self, statusf, custof, descricaof, codf):
        return self._processosF.inserir_fila(statusf, custof, descricaof, codf)


    def remover_processo_P(self):
        return self._processosP.remover_pilha()


    def remover_processo_L(self, posicao):
        return self._processosL.remover_lista(posicao)


    def remover_processo_F(self):
        return self._processosF.remover_fila()


    def busca_processo_l(self, codigo):
        return self._processosL.buscar(codigo)


    def ordena_processos(self):
        return self._processosL.ordenar()


    def imprimir_processos_l(self):
        saida = ''
        ponteirinho = self._processosL.posicao0

        while ponteirinho != None:
            saida += f'Status: {ponteirinho.status} — Código:{c[19]}{ponteirinho.cod}{c[0]}\n'
            ponteirinho = ponteirinho.prox

        return saida


    def mostrar_tam_processosL(self):
        return self._processosL.tamanho_lista()


    def mostrar_tam_processosP(self):
        return self._processosP.tamanho_pilha()
        

    def mostrar_tam_processosF(self):
        return self._processosF.tamanho_fila()
        