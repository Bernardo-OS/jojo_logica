#Uma bomba possui 6 fios:

#Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)

#O sistema interno da bomba foi programado usando lógica proposicional.

#O jogador recebe um conjunto de pistas.

#Seu objetivo é descobrir quais fios cortar e em que ordem.

#Bomba explode se o tempo acabar ou se errar o fio.

import sys
import threading
import time

import msvcrt

import Desafio


#######CONTROLE DE TEMPO############
intervalo_aviso = 15

def ler_entrada_com_tempo_limite(mensagem, evento_fim, tempo_inicio):
    print(mensagem, end="", flush=True)
    entrada = []

    while not evento_fim.is_set():
        if msvcrt.kbhit():
            caractere = msvcrt.getwch()

            if caractere in ("\r", "\n"):
                print()
                return "".join(entrada).strip()

            if caractere == "\b":
                if entrada:
                    entrada.pop()
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                continue

            entrada.append(caractere)
            sys.stdout.write(caractere)
            sys.stdout.flush()

        if time.time() - tempo_inicio >= tempo_limite:
            evento_fim.set()
            break

        time.sleep(0.05)

    print()
    return None


def controlar_tempo(evento_fim, tempo_inicio):
    proximo_aviso = intervalo_aviso

    while not evento_fim.is_set():
        tempo_decorrido = time.time() - tempo_inicio

        if tempo_decorrido >= tempo_limite:
            print("Tempo esgotado! A bomba explodiu!")
            evento_fim.set()
            break

        if tempo_decorrido >= proximo_aviso:
            tempo_restante = max(0, int(tempo_limite - tempo_decorrido))
            print(f"\n{tempo_restante} segundos restantes.")
            proximo_aviso += intervalo_aviso

        time.sleep(0.2)
###################################

print("Bem-vindo ao jogo da bomba lógica")
print("Você precisa cortar os fios na ordem correta para desarmar a bomba.")
print("Pistas do funcionamento da bomba serão fornecidas em forma de proposições lógicas para ajudá-lo a descobrir a sequência correta com os códigos correspondentes:")
print("Vermelho (R), Azul (B), Verde (G), Amarelo (Y), Branco (W), Preto (K)")
print("Levando em consideração que as proposições devem dar valor verdadeiro para a bomba desarmar sem explodir.")
print("O valor positivo significa no caso desconectá-lo do circuito, você deve preencher em sequência de acordo com a solução das proposições os fios que cortar corretamente.")
numero_desafio = input("Coloque o número correspondente ao desafio que deseja jogar (1, 2, 3, 4 ou 5) e pressione Enter: ")
desafio = Desafio.Desafio(0, "", [], 0)
desafio = desafio.obter_desafio_por_numero(numero_desafio)
if desafio is None:
    print("Número de desafio inválido. Encerrando o jogo.")
    sys.exit(1)
tempo_limite = desafio.tempo  # segundos
print("As pistas são as seguintes:")
print(desafio.pistas)

sequencia_correta = desafio.dividir_fios(desafio.sequencia)
#sequencia_correta = ["R", "B", "G", "Y"]
inicio = time.time()
evento_fim = threading.Event()
thread_tempo = threading.Thread(target=controlar_tempo, args=(evento_fim, inicio), daemon=True)
thread_tempo.start()

i = 0

while not evento_fim.is_set() and i < len(sequencia_correta):
    resposta = ler_entrada_com_tempo_limite(
        "Digite o próximo fio a cortar (r, b, g, y, w, k): ",
        evento_fim,
        inicio,
    )

    if resposta is None:
        break

    resposta = resposta.upper()

    if resposta != sequencia_correta[i]:
        print("Fio incorreto! Bomba expludiu! A sequência correta era:", sequencia_correta)
        evento_fim.set()
        break

    i += 1
    print("Fio correto!")

    if i == len(sequencia_correta):
        print("Parabéns! Você desarmou a bomba com sucesso!")
        evento_fim.set()
        break


#if not evento_fim.is_set() and i < len(sequencia_correta):
if i < len(sequencia_correta) and not evento_fim.is_set():
    print("Tempo esgotado. A bomba explodiu! A sequência correta era:", sequencia_correta)
