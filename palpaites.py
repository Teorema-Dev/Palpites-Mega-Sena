from random import randint


def sorteando():
    lista = list()
    jogos = list()
    quant = 1
    tot = 1  # Total de vezes que vai sortear
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:  # Se o n° não estiver na lista,
                lista.append(num)  # Adicionar
                cont += 1  # Variável contador recebe + 1
            if cont >= 6:  # Se a variável contador for maior ou igual a 6
                break  # Finaliza o laço de repetição
        lista.sort()
        jogos.append(lista[:])  # criando cópia da lista
        tot += 1
        return lista


sorteando()
print(sorteando())