import calculo as ca


def menu(cadastro):
    try:
        menu_pri = int(input(cadastro))
        if menu_pri == 1:
            return True
        elif menu_pri == 2:
            return exibir()
        elif menu_pri == 3:
            return menu_pri
        else:
            print('Dado inválido')
            return menu(cadastro)
    except:
        print('Dado inválido')
        return menu(cadastro)


def sabores(opc):
    try:
        sabor = int(input(opc))
        if sabor == 1 or sabor == 2 or sabor == 3 or sabor == 4 or sabor == 5 or sabor == 6:
            return sabor
        else:
            print('Dado inválido')
            return sabores(opc)
    except:
        print('Dado inválido')
        return sabores(opc)


def tamanho(tama):
    try:
        tam = int(input(tama))
        if tam == 1 or tam == 2 or tam == 3 or tam == 4:
            return tam
        else:
            print('Dado inválido')
            return tamanho(tama)
    except:
        print('Dado inválido')
        return tamanho(tama)


def quantidade(qtdp):
    try:
        qtd = int(input(qtdp))
        if qtd > 3:
            return qtd
        elif 0 < qtd <= 3:
            return qtd
        else:
            print('Dado inválido')
            return quantidade(qtdp)
    except:
        print('Dado inválido')
        return quantidade(qtdp)


def mais_pizza(opc_mais):
    try:
        mais_p = input(opc_mais).upper()
        if mais_p == 'S':
            return 0
        elif mais_p == 'N':
            return 1
        else:
            print('Dado inválido')
            return mais_pizza(opc_mais)
    except:
        print('Dado inválido')
        return mais_pizza(opc_mais)


def salvar(sabor, tam, qtd, frete, val_tot, nome):
    arquivo = open('Pedidos.txt', 'a+')
    arquivo.write('\nCliente: ' + nome)
    arquivo.write('\nSabor: ' + str(ca.sabores_pizza[sabor - 1][0]))
    arquivo.write('\nTamanho: ' + str(ca.tamanhos[tam - 1][0]))
    arquivo.write('\nQuantidade: ' + str(qtd))
    arquivo.write('\nFrete:' + str(frete))
    arquivo.write('\nValor: R$' + str(val_tot))
    arquivo.write('\n')


def exibir():
    arquivo = open('Pedidos.txt', 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()
