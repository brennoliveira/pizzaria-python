sabores_pizza = [('Mozzarela', 25), ('Calabresa', 25), ('A moda da casa', 30),
                 ('Baiana', 30), ('Portuguesa', 30), ('Frango com catupiry', 35)]

tamanhos = [('Pequena', 0), ('Média', 5), ('Grande', 7), ('Família', 11)]


def valor(sabor, tam):
    val = sabores_pizza[sabor - 1][1] + tamanhos[tam - 1][1]
    return val


def frete(qtd):
    if qtd > 3:
        frete = 0
        return frete
    elif qtd <= 3:
        frete = 5
        return frete


def valor_total(frete, val, qtd):
    val_tot = (val * qtd) + frete
    return val_tot
