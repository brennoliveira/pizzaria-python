import utilitarios as ut
import calculo as ca

while True:
    cadastro = '''Menu:
==============================
    [1]Pedir
    [2]Listar pedidos
    [3]Sair
==============================
O que deseja fazer?'''
    menu_pri = ut.menu(cadastro)
    if menu_pri == 3:
        print('Volte sempre')
        break
    while menu_pri == True:
        nome = input('Seu nome:')
        tama = '''Tamanhos:
==============================
    [1]Pequena + R$0.00
    [2]Média + R$5.00
    [3]Grande + R$7.00
    [4]Família + R$11.00
==============================
Qual tamanho?'''
        opc = '''Sabores:
==============================
    [1]Mozzarela: R$25.00
    [2]Calabresa: R$25.00
    [3]A moda da casa: R$30.00
    [4]Baiana: R$30.00
    [5]Portuguesa: R$30.00
    [6]Frango com catupiry: R$35.00
==============================
Qual o sabor?'''
        qtdp = 'Quantidade?'
        opc_mais = 'Quer pedir mais?'
        sabor = ut.sabores(opc)
        tam = ut.tamanho(tama)
        qtd = ut.quantidade(qtdp)
        mais_p = ut.mais_pizza(opc_mais)
        if mais_p == 0:
            val = ca.valor(sabor, tam)
            frete = ca.frete(qtd)
            val_tot = ca.valor_total(frete, val, qtd)
            ut.salvar(sabor, tam, qtd, frete, val_tot, nome)

        elif mais_p == 1:
            val = ca.valor(sabor, tam)
            frete = ca.frete(qtd)
            val_tot = ca.valor_total(frete, val, qtd)
            ut.salvar(sabor, tam, qtd, frete, val_tot, nome)
            ut.exibir()
            break
