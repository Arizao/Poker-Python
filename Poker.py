# Comentário:
# Inicio do programa de poker:

import random
import itertools

num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
naipes = ["D", "S", "H", "C"]
val = []
seq = []

incremento1 = 2
incremento2 = 2


for numero in num:
    val.append(incremento2)
    incremento2 = incremento2 + 1

    for naipe in naipes:
        seq.append(incremento1)
        incremento1 = incremento1 + 1


class _carta:

    # Classe carta ( Número, naipe, valor)

    def __init__(self, _numero, _naipe, _valor, _sequencia):
        self.numero = _numero
        self.naipe = _naipe
        self.valor = _valor
        self.sequence = _sequencia


def gera_mao():

    mao = []

    for n in range(5):

        naipe = random.choice(naipes)
        valor = random.choice(val)
        numero = num[valor-2]
        sequencia = seq[(valor - 2)*(naipes.index(naipe) + 1)]
        mao.append(_carta(numero, naipe, valor, sequencia))
    
    return mao


mao1 = gera_mao()
mao2 = gera_mao()

print(mao1[0].numero + mao1[0].naipe, mao1[1].numero + mao1[1].naipe, mao1[2].numero +
      mao1[2].naipe, mao1[3].numero + mao1[3].naipe, mao1[4].numero + mao1[4].naipe)
print(mao2[0].numero + mao2[0].naipe, mao2[1].numero + mao2[1].naipe, mao2[2].numero +
      mao2[2].naipe, mao2[3].numero + mao2[3].naipe, mao2[4].numero + mao2[4].naipe)

def calcula_força(mao):

    conferidor_sequencia = 0
    conferidor_naipe = 0
    conferidor_carta_igual = 0
    força = 0

    mao_crescente = sorted([mao[0].valor, mao[1].valor, mao[2].valor, mao[3].valor, mao[4].valor])
    força_mao = (5*(mao[0].valor + mao[1].valor + mao[2].valor + mao[3].valor + mao[4].valor))

    for n in range(4):
        if (mao_crescente[n] + 1) == mao_crescente[n + 1]:
            conferidor_sequencia = conferidor_sequencia + 1


    for n in range(len(mao)-1):
        for m in range(len(mao)-n-1):
            if mao[n].valor == mao[n+m+1].valor:
                conferidor_carta_igual = conferidor_carta_igual + 1

            if mao[n].naipe == mao[n+m+1].naipe:
                conferidor_naipe = conferidor_naipe + 1


    if conferidor_sequencia == 4:

        if conferidor_naipe == 5 and mao_crescente[4] == 14:
            força = 10000
            #Royal Flush

        elif conferidor_naipe == 5:
            força = 9000
            # Straight flush

        else:
            força = 5000
            # Straight

    elif conferidor_naipe == 5:
        força = 6000
        # Flush

    if conferidor_carta_igual == 1:
        força = 2000
        # Par

    elif conferidor_carta_igual == 2:
        força = 3000
        # Double Par

    elif conferidor_carta_igual == 3:
        força = 4000
        # Trinca

    elif conferidor_carta_igual == 4:
        força = 7000
        # Full House

    elif conferidor_carta_igual == 6:
        força = 8000
        # Quadra

    força_mao_final = força + força_mao

    return força_mao_final


força_mao1_final = calcula_força(mao1)
força_mao2_final = calcula_força(mao2)

print(força_mao1_final)
print(força_mao2_final)

if força_mao1_final > força_mao2_final:
    print("Jogador 1 é o vencedor")

elif força_mao1_final < força_mao2_final:
    print("Jogador 2 é o vencedor")

else:
    print("Empate das mãos")
