#Uma bomba possui 6 fios:

#Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)

#O sistema interno da bomba foi programado usando lógica proposicional.

#O jogador recebe um conjunto de pistas.

#Seu objetivo é descobrir quais fios cortar e em que ordem.

#Cada erro diminui o tempo restante.

import time

tempo_limite = 60  # segundos



print("Bem-vindo ao jogo da bomba lógica")
print("Você precisa cortar os fios na ordem correta para desarmar a bomba.")
print("Pistas do funcionamento da bomba serão fornecidas em forma de proposições lógicas para ajudá-lo a descobrir a sequência correta com os códigos correspondentes:")
print("Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)")
print("Levando em consideração que as proposições devem dar valor verdadeiro para a bomba desarmar sem explodir.")
print("O valor positivo significa no caso desconectá-lo do circuito, você deve preencher em sequência de acordo com a solução das proposições os fios que cortar corretamente.")
input("Pressione Enter para começar o jogo")
print("As pistas são as seguintes:")
print("1) R → B \n2) ~(R ∧ G) \n3) B ∨ G \n4) Y → B \n5) R")
sequencia_correta = ["R", "B", "G", "Y"]  # Sequência correta de fios a cortar
inicio = time.time()




while True:
    tempo_decorrido = time.time() - inicio
    if tempo_decorrido >= tempo_limite:
        print("Tempo esgotado! A bomba explodiu!")
        break

    resposta = input("Digite a sequência de fios a cortar (ex: RBGY): ").upper()

    if i > sequencia_correta.len:
        print("Parabéns! Você desarmou a bomba com sucesso!")
        break
    else:
        print("Sequência incorreta! Tente novamente.")
tempo_restante = int(tempo_limite - (time.time() - inicio))
print(f"Tempo restante: {tempo_restante}s")