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

    #Classe carta ( Número, naipe, valor)

    def __init__(self,_numero,_naipe,_valor,_sequencia):
        self.numero = _numero
        self.naipe = _naipe
        self.valor = _valor
        self.sequence = _sequencia
    

mao1 = []
mao2 = []

for n in range(5):
        
    naipe = random.choice(naipes)
    valor = random.choice(val)
    numero = num[valor-2]
    sequencia = seq[(valor - 2)*(naipes.index(naipe) + 1)]
    mao1.append(_carta(numero, naipe, valor, sequencia))

for n in range(5):

    naipe = random.choice(naipes)
    valor = random.choice(val)
    numero = num[valor-2]
    sequencia = seq[(valor - 2)*(naipes.index(naipe) + 1)]
    mao2.append(_carta(numero, naipe, valor, sequencia))

print(mao1[0].numero + mao1[0].naipe, mao1[1].numero + mao1[1].naipe, mao1[2].numero + mao1[2].naipe, mao1[3].numero + mao1[3].naipe, mao1[4].numero + mao1[4].naipe)
print(mao2[0].numero + mao2[0].naipe, mao2[1].numero + mao2[1].naipe, mao2[2].numero + mao2[2].naipe, mao2[3].numero + mao2[3].naipe, mao2[4].numero + mao2[4].naipe)

mao1_crescente = sorted([mao1[0].valor, mao1[1].valor, mao1[2].valor, mao1[3].valor, mao1[4].valor])
mao2_crescente = sorted([mao2[0].valor, mao2[1].valor, mao2[2].valor, mao2[3].valor, mao2[4].valor])

força_mao1 = (5*(mao1[0].valor + mao1[1].valor + mao1[2].valor + mao1[3].valor + mao1[4].valor))
força_mao2 = (5*(mao2[0].valor + mao2[1].valor + mao2[2].valor + mao2[3].valor + mao2[4].valor))

print(mao1_crescente, mao2_crescente)

#Análise da Mão 1:

conferidor_sequencia1 = 0
conferidor_naipe1 = 0
conferidor_carta_igual1 = 0
força1 = 0

print(força_mao1, força_mao2)

for n in range (4):
    if (mao1_crescente[n] + 1) == mao1_crescente[n + 1]:
        conferidor_sequencia1 = conferidor_sequencia1 + 1


for n in range(len(mao1)-1):
    for m in range(len(mao1)-n-1):
        if mao1[n].valor == mao1[n+m+1].valor:
            conferidor_carta_igual1 = conferidor_carta_igual1 + 1
        
        if mao1[n].naipe == mao1[n+m+1].naipe:
            conferidor_naipe1 = conferidor_naipe1 + 1

        
if conferidor_sequencia1 == 4:

    if conferidor_naipe1 == 5 and mao1_crescente[4] == 14:
        força1 = 10000
        #Royal Flush

    elif conferidor_naipe1 == 5:
        força1 = 9000
        #Straight flush

    else:
        força1 = 5000
        #Straight

elif conferidor_naipe1 == 5:
    força1 = 6000 
    #Flush

if conferidor_carta_igual1 == 1:
    força1 = 2000
    #Par

elif conferidor_carta_igual1 == 2:
    força1 = 3000
    #Double Par

elif conferidor_carta_igual1 == 3:
    força1 = 4000
    #Trinca

elif conferidor_carta_igual1 == 4:
    força1 = 7000
    #Full House

elif conferidor_carta_igual1 == 6:
    força1 = 8000
    #Quadra

força_mao1_final = força1 + força_mao1

#Análise Mão 2:

conferidor_sequencia2 = 0
conferidor_naipe2 = 0
conferidor_carta_igual2 = 0
força2 = 0


for n in range (4):
    if (mao2_crescente[n] + 1) == mao2_crescente[n + 1]:
        conferidor_sequencia2 = conferidor_sequencia2 + 1




for n in range(len(mao2)-1):
    for m in range(len(mao2)-n-1):
        if mao2[n].valor == mao2[n+m+1].valor:
            conferidor_carta_igual2 = conferidor_carta_igual2 + 1
        
        if mao2[n].naipe == mao2[n+m+1].naipe:
            conferidor_naipe2 = conferidor_naipe2 + 1

        
if conferidor_sequencia2 == 4:

    if conferidor_naipe2 == 5 and mao2_crescente[4] == 14:
        força2 = 10000
        #Royal Flush

    elif conferidor_naipe2 == 5:
        força2 = 9000
        #Straight flush

    else:
        força2 = 5000
        #Straight

elif conferidor_naipe2 == 5:
    força2 = 6000 
    #Flush

if conferidor_carta_igual2 == 1:
    força2 = 2000
    #Par

elif conferidor_carta_igual2 == 2:
    força2 = 3000
    #Double Par

elif conferidor_carta_igual2 == 3:
    força2 = 4000
    #Trinca

elif conferidor_carta_igual2 == 4:
    força2 = 7000
    #Full House

elif conferidor_carta_igual2 == 6:
    força2 = 8000
    #Quadra

força_mao2_final = força2 + força_mao2



print(força_mao1_final)
print(força_mao2_final)

if força_mao1_final > força_mao2_final:
    print("Jogador 1 é o vencedor")

elif força_mao1_final < força_mao2_final:
    print("Jogador 2 é o vencedor")

else:
    print("Empate das mãos")
