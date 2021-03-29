from frufru import *
from advogado import *
from fila import *
from pilha import *
from processo import *

# -------------------------------------------------------------- OBJETOS --------------------------------------------------------------
advogado = Advogado('10123')
# Lista
advogado.adicionar_processo_L('Em trâmite', 3000, 'Processo relacionado a Ação de Alimentos Gravídicos', 350987, 1)
advogado.adicionar_processo_L('Em trâmite', 2500, 'Processo relacionado a Ação de Divórcio Litigioso', 330987, 2)
advogado.adicionar_processo_L('Em trâmite', 1500, 'Processo relacionado a Ação de Guarda Compartilhada', 320987, 2)
advogado.adicionar_processo_L('Finalizado', 2000, 'Processo relacionado a Ação de Inventário e Partilha', 370987, 1)
advogado.adicionar_processo_L('Em trâmite', 5000, 'Processo relacionado a Ação de Despejo por Falta de Pagamento', 390987, 2)

# Pilha
advogado.adicionar_processo_P('Em trâmite', 4950, 'Processo relacionado a Ação Negatória de Paternidade', 430987)
advogado.adicionar_processo_P('Finalizado', 2000, 'Processo relacionado a Ação de Usucapião', 450987)
advogado.adicionar_processo_P('Em trâmite', 1500, 'Processo relacionado a Ação Reivindicatória de Herança', 420987)
advogado.adicionar_processo_P('Em trâmite', 2500, 'Processo relacionado a Ação Revisional de Financimanto de Veículo', 440987)
advogado.adicionar_processo_P('Em trâmite', 5000, 'Processo relacionado a Ação de Bloqueio de Bens', 460987)

# Fila
advogado.adicionar_processo_F('Em trâmite', 1500, 'Processo relacionado a Ação Indenizatória por Danos Morais', 520987)
advogado.adicionar_processo_F('Em trâmite', 2500, 'Processo relacionado a Ação Declaratória de Alienação Parental', 540987)
advogado.adicionar_processo_F('Em trâmite', 5000, 'Processo relacionado a Ação Indenizatória de Danos Materiais', 560987)
advogado.adicionar_processo_F('Em trâmite', 4990, 'Processo relacionado a Ação de Reintegração de Posse', 530987)
advogado.adicionar_processo_F('Finalizado', 2000, 'Processo relacionado a Ação para Fornecimento de Medicamento de Alto Custo', 550987)

#----------------------------------------------------------------------------------------------------------------------------------------


print(f'*' * 50)
print(f"{c[10]}{'MINI-SISTEMA JURÍDICO - 2.0':^50}{c[0]}")
print(f'*' * 50)

while True:
    resp = menu(["Buscar o processo de maior custo da lista", "Buscar o processo de menor custo da lista", "Incrementar valor no custo de um processo da lista", "Adicionar novo processo a pilha", "Adicionar novo processo a lista", "Adicionar novo proceso a fila","Remover processo da pilha", "Remover processo da lista", "Remover processo da fila", "Buscar processo da lista pelo código", "Ordenar processos da lista", "Impressão dos processos da lista", "Exibir o tamanho da lista de processos", "Mostrar o tamanho da pilha de processos", "Apresentar o tamanho da fila de processos","Sair do Sistema"],"MENU PRINCIPAL")
    if resp == 1:
        try:
            print(f'{c[27]}\nO processo de maior custo da lista apresenta:{c[0]}')
            maiorzito = advogado.maior_custo()
            print(f'  Status: {maiorzito.status}\n  Código: {maiorzito.cod}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except ListaException:
            print(f'{c[30]}A lista está vazia!{c[0]}')


    if resp == 2:
        try:
            print(f'{c[27]}\nO processo de menor custo da lista apresenta:{c[0]}')
            menorzito = advogado.menor_custo()
            print(f'  Status: {menorzito.status}\n  Código: {menorzito.cod}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except ListaException:
            print(f'{c[30]}A lista está vazia!{c[0]}')


    if resp == 3:
        try:
            if advogado.processosL.tamanho_lista() != 0:
                print('\nSabendo que os processos da lista possuem os seguintes códigos:')
                printa = ''
                for i in range(advogado.processosL.tamanho_lista()):
                    printa += f'[{advogado.processosL.mostrar_elemento_lista(i).cod}] '
                print(printa)
                valor_add = int(input('\nInforme o valor a ser incrementado ao custo: R$'))
                qual_processo = int(input('Informe o codigo do processo: '))
                procss = advogado.busca_processo_l(qual_processo)
                if qual_processo == procss.cod:
                    advogado.incrementa_custo_processo_l(qual_processo, valor_add)
                    print(
                        f'{c[18]}O valor de R$ {valor_add} foi incrementado ao processo de código[{qual_processo}]!{c[0]}')
            else:
                print(f'{c[19]}A lista está vazia!{c[0]}')
        except ValueError:
            print(f'{c[30]}Informe um valor válido!{c[0]}')
        except AttributeError:
            print(f'{c[30]}Informe um código válido!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')


    if resp == 4:
        try:
            statusy = str(input('Informe o status: '))
            custoy = int(input('Informe o custo: R$'))
            descricaoy = str(input('Informe a descrição: '))
            cody = int(input('Informe o código:'))
            advogado.adicionar_processo_P(statusy, custoy, descricaoy, cody)
        except ValueError:
            print(f'{c[30]}Digite informações válidas!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')


    if resp == 5:
        try:
            statusz = str(input('Informe o status do processo: '))
            custoz = int(input('Informe o custo do processo: R$'))
            descricaoz = str(input('Informe a descrição do processo: '))
            codz = int(input('Informe o código do processo: '))
            posicaoz = int(input(f'Informe a posição do processo: [>0 e <={advogado.mostrar_tam_processosL()+1}] '))
            if (posicaoz < 0) or (posicaoz > (advogado.mostrar_tam_processosL()+1)):
                print(f'{c[19]}Posição inválida{c[0]}')
            else:
                advogado.adicionar_processo_L(statusz, custoz, descricaoz, codz, posicaoz)
        except ValueError:
            print(f'{c[30]}Digite informações válidas!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')


    if resp == 6:
        try:
            statusx = str(input('Informe o status: '))
            custox = int(input('Informe o custo: R$'))
            descricaox = str(input('Informe a descrição: '))
            codx = int(input('Informe o código:'))
            advogado.adicionar_processo_F(statusx, custox, descricaox, codx)
        except ValueError:
            print(f'{c[30]}Digite informações válidas!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')


    if resp == 7:
        try:
            print(advogado.processosP)
            advogado.remover_processo_P()
            print(f'\n{advogado.processosP}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except PilhaException:
            print(f'{c[30]}Pilha já está vazia!{c[0]}')


    if resp == 8:
        try:
            print(advogado.processosL)
            remov_l = int(input(f'\nInforme a posição do processo que deseja remover da lista [escolha entre 1 e {advogado.mostrar_tam_processosL()}]: '))
            if (remov_l < 0) or (remov_l > advogado.mostrar_tam_processosL()):
                print(f'{c[19]}Posição inválida!{c[0]}')
            else:
                advogado.remover_processo_L(remov_l)
                print(f'\n{advogado.processosL}')
        except IndexError:
            print(f'{c[30]}Informe um número válido!{c[0]}')
        except ValueError:
            print(f'{c[30]}Informe um valor válido!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except ListaException:
            print(f'{c[30]}A lista já está vazia!{c[0]}')


    if resp == 9:
        try:
            print(advogado.processosF)
            advogado.remover_processo_F()
            print(f'\n{advogado.processosF}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except FilaException:
            print(f'{c[30]}A fila já está vazia!{c[0]}')


    if resp == 10:
        try:
            if advogado.processosL.tamanho_lista() != 0:
                print(f'\nDadas as opções :')
                printa = ''
                for i in range(advogado.processosL.tamanho_lista()):
                    printa += f'[{advogado.processosL.mostrar_elemento_lista(i).cod}] '
                print(printa)
                buscar_processo = int(input("\nInforme o código do processo que deseja acessar:"))
                buscado = advogado.busca_processo_l(buscar_processo)
                print(
                    f'\n{c[31]}O processo que tem o cod {buscado.cod} apresenta:{c[0]}\n  Status: {buscado.status}\n  Custo: R$ {buscado.custo}\n  Descrição: {buscado.descricao}\n  Código: {buscado.cod}')
            else:
                print(f'{c[19]}A lista está vazia!{c[0]}')
        except ValueError:
            print(f'{c[30]}Informe um valor válido!{c[0]}')
        except AttributeError:
            print(f'{c[30]}Informe um código válido!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
       

    if resp == 11:
        try:
            advogado.ordena_processos()
            print(f'{c[31]}Lista ordenada com sucesso!{c[0]}')
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except ListaException:
            print(f'{c[30]}A lista está vazia!{c[0]}')


    if resp == 12:
        try:
            print(advogado.imprimir_processos_l())
        except NameError:
            print(f'{c[30]}Nenhum processo/advogado está cadastrado!{c[0]}')
        except ListaException:
            print(f'{c[30]}A lista está vazia!{c[0]}')


    if resp == 13:
        try:
            print('O tamanho da lista de processos é:', advogado.mostrar_tam_processosL())
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')


    if resp == 14:
        try:
            print('O tamanho da pilha de processos é:', advogado.mostrar_tam_processosP())
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')


    if resp == 15:
        try:
            print('O tamanho da fila de processos é: ', advogado.mostrar_tam_processosF())
        except NameError:
            print(f'{c[30]}Nenhum advogado está cadastrado!{c[0]}')

    if resp == 16:
        cabecalho('ATÉ LOGO!')
        break
