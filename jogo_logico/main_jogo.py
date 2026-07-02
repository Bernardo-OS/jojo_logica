#Uma bomba possui 6 fios:

#Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)

#O sistema interno da bomba foi programado usando lógica proposicional.

#O jogador recebe um conjunto de pistas.

#Seu objetivo é descobrir quais fios cortar e em que ordem.

#Cada erro diminui o tempo restante.

import time

tempo_limite = 180  # segundos



print("Bem-vindo ao jogo da bomba lógica")
print("Você precisa cortar os fios na ordem correta para desarmar a bomba.")
print("Pistas do funcionamento da bomba serão fornecidas em forma de proposições lógicas para ajudá-lo a descobrir a sequência correta com os códigos correspondentes:")
print("Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)")
print("Levando em consideração que as proposições devem dar valor verdadeiro para a bomba desarmar sem explodir.")
print("O valor positivo significa no caso desconectá-lo do circuito, você deve preencher em sequência de acordo com a solução das proposições os fios que cortar corretamente.")
input("Pressione Enter para começar o jogo")
print("As pistas são as seguintes:")
print("(1) R → B \n (2) ~(R ∧ G) \n(3) B ∨ G \n(4) Y → B \n(5) R")
sequencia_correta = ["R", "B", "G", "Y"]  # Sequência correta de fios a cortar
inicio = time.time()

"""
tempo_decorrido = time.time() - inicio
    if tempo_decorrido >= tempo_limite:
        print("Tempo esgotado! A bomba explodiu!")
        break
"""

while time.time() - inicio < tempo_limite:
    tempo_restante = int(tempo_limite - (time.time() - inicio))
    i = 0
    resposta = input("Digite o próximo fio a cortar (r, b, g, y, w, k): ").upper()
    i+=1

    if resposta != sequencia_correta[i]:
        print("Fio incorreto!")
        break

    if i == len(sequencia_correta) and sequencia_correta[i] == resposta:
        print("Parabéns! Você desarmou a bomba com sucesso!")
        break
    else:
        print("Sequência incorreta! Tente novamente.")
        
if tempo_restante <= 0:
    print("Tempo esgotado!")
print("Bomba explodiu! A sequência correta era:", sequencia_correta)



    '''
    print(f"Tempo restante: {tempo_restante}s")
    '''
