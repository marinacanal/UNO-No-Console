# Marina Canal e Luiz Gustavo
# Ciência da Computação - Noturno 
# UFFS - Campus Chapeco

import random
import os
import sys

cores_ansi = {
    "Azul": "\033[34m",  # azul
    "Vermelho": "\033[31m",  # vermelho
    "Amarelo": "\033[33m",  # amarelo
    "Verde": "\033[32m",  # verde
    "Reset": "\033[0m"  # resetar cor para o padrão
}

# criar baralho
def criar_baralho():
  cores = ["Azul","Vermelho","Amarelo","Verde"]
  numeros = [1,2,3,5,6,7,8,9]

  baralho = []

  for cor in cores:
    for numero in numeros:
      baralho.append((cor, numero)) # adiciona na matriz baralho uma tupla com a cor e o numero (a carta)

  return embaralhar_baralho(baralho)


# embaralhar baralho
def embaralhar_baralho(baralho):

  for posicao in range(len(baralho) - 1, 0, -1):
    posicao_aleatorio = random.randint(0,posicao)

    # troca os valores das posições, ex: baralho[1] = baralho[2] e baralho[2] = baralho[1]
    baralho[posicao], baralho[posicao_aleatorio] = baralho[posicao_aleatorio], baralho[posicao]

  return baralho


# distribuir cartas
def distribuir_cartas(quantidade_jogadores, jogadores, baralho):
  maos = {}

  #só cria as mãos, sem nada dentro
  for i in range(quantidade_jogadores):
    jogador = jogadores[i]
    maos[jogador] = []

  #distribui 5 cartas para cada jogador
  for i in range(5 * quantidade_jogadores):
    jogador_atual = jogadores[i % quantidade_jogadores]
    maos[jogador_atual].append(baralho[i])

  return maos


# pescar ou jogar carta
def pescar_ou_jogar_carta(baralho, pilha_mesa, carta_na_mesa, jogador, maos):
  resposta = input((f"\n{jogador}, digite o número da carta que você deseja jogar ou [P] para pescar: "))

  # se o usuario jogar uma carta
  if resposta != 'P':

    index_carta = int(resposta)

    carta = maos[jogador][index_carta]

    # verifica se a cor ou numero da carta procede
    if carta[0] == carta_na_mesa[0] or carta[1] == carta_na_mesa[1]:

        carta_na_mesa = maos[jogador].pop(index_carta) # tira carta da mao do jogador
        pilha_mesa.append(carta_na_mesa) # adiciona na pilha da mesa
        print(f"\ncarta na mesa: {cores_ansi[carta_na_mesa[0]]} {carta_na_mesa[0]} {carta_na_mesa[1]} {cores_ansi['Reset']}")

        if len(maos[jogador]) <= 0:
          terminar_jogo(jogador)

    else:
        print("\n--- carta inválida! ---")
        pescar_ou_jogar_carta(baralho, pilha_mesa, carta_na_mesa, jogador, maos)

  else:
    carta_pescada = baralho.pop() # retira uma carta do baralho

    if carta_pescada != '': # se o baralho nao acabou

      print(f"\ncarta pescada: {cores_ansi[carta_pescada[0]]} {carta_pescada[0]} {carta_pescada[1]} {cores_ansi['Reset']}")
      print(f"\ncarta na mesa: {cores_ansi[carta_na_mesa[0]]} {carta_na_mesa[0]} {carta_na_mesa[1]} {cores_ansi['Reset']}")

      maos[jogador].append(carta_pescada) # adiciona na mao do jogador

    else:
      terminar_jogo('')

      return False

  return baralho, maos, carta_na_mesa


# terminar jogo
def terminar_jogo(jogador):
  os.system("clear")

  if jogador != '':

    print(".______      ___       .______          ___      .______    _______  .__   __.   _______. " +
        "\n|   _  \\   /   \\     |   _  \\      /   \\     |   _  \\ |   ____| |  \\ |  | /       | " +
        "\n|  |_)  |  /  ^  \\    |  |_)  |     /  ^  \\    |  |_)  | |  |__    |   \\|  | |   (----`" +
        "\n|   ___/  /  /_\\ \\   |      /     /  /_\\ \\   |   _  <  |   __|   |  . `   |  \\    \\ " +
        "\n|  |     /  _____  \\  |  |\\ \\--./  _____  \\  |  |_)  | |  |____  |  |\\   | .----)   |" +
        "\n| _|    /__/    \\__\\ | _| `.____/__/    \\__\\ |______/  |_______| |__| \\__| |_______/ ")

    print(f"\n{jogador} venceu o jogo!")

  else:
    print(" _______  .___  ___. .______      ___   .__________.  _______ " +
        "\n|   ____| |   \/   | |   _  \    /   \  |          | |   ____|" +
        "\n|  |__    |  \  /  | |  |_)  |  /  ^  \ `---|  |---` |  |__   " +
        "\n|   __|   |  |\/|  | |   ___/  /  /_\  \    |  |     |   __|  " +
        "\n|  |____  |  |  |  | |  |     /  _____  \   |  |     |  |____ " +
        "\n|_______| |__|  |__| | _|    /__/     \__\  |__|     |_______|")

    print("\nempate! o baralho acabou")

  print("\n\n\ndeseja jogar novamente? [S/N]")
  jogar = input()

  if jogar == "S":
      jogar_uno()  # reinicia o jogo

  return


# jogar uno
def jogar_uno():

  os.system("clear")

  print("bem vindo ao jogo")

  print("__    __  .__   __.   ______   " +
     "\n|  |  |  | |  \ |  |  /  __  \  " +
     "\n|  |  |  | |   \|  | |  |  |  | " +
     "\n|  |  |  | |  . `  | |  |  |  | " +
     "\n|  `--'  | |  |\   | |  `--'  | " +
     "\n \______/  |__| \__|  \______/ \n")

  print("feito por: Marina && Luiz")

  quantidade_jogadores = int(input("\n\npor favor, digite a quantidade de jogadores (1-4): "))

  if quantidade_jogadores > 0:

    jogadores = [] # inicializa variavel
    print()

    # solicita o nome de cada jogador
    for contador in range(1,quantidade_jogadores + 1):
      jogadores.append((input(f"digite o nome do jogador {contador}: ")))

    baralho = criar_baralho() # baralho criado
    pilha_mesa = [] # inicializa a pilha de cartas que vai existir na mesa

    maos = distribuir_cartas(quantidade_jogadores, jogadores, baralho) # distribui cartas

    os.system("clear")

    print("\ncartas distribuídas!")

    carta_na_mesa = baralho.pop() # tira primeira carta
    pilha_mesa.append(carta_na_mesa) # coloca na pilha da mesa

    print(f"\ncarta na mesa: {cores_ansi[carta_na_mesa[0]]} {carta_na_mesa[0]} {carta_na_mesa[1]} {cores_ansi['Reset']}")

    while True:

      for jogador in jogadores:
        index_jogador = jogadores.index(jogador)

        if len(maos[jogador]) > 0:

          print("\n----------------------------")

          # mostra as cartas da mao do jogador
          print(f"\nmão de {jogador}: ")

          for index, (cor, numero) in enumerate(maos[jogador]):
            cor_ansi = cores_ansi.get(cor, cores_ansi["Reset"])
            print(f'{index} - {cor_ansi} {cor} {numero} {cores_ansi["Reset"]}')

          # pede para o usuario jogar ou pescar uma carta
          baralho, maos, carta_na_mesa = pescar_ou_jogar_carta(baralho, pilha_mesa, carta_na_mesa, jogador, maos)

        else:
          terminar_jogo(jogador)

          return False
  else:
    print("\na quantidade de jogadores precisa estar entre 1-4 para jogar!")
    jogar = input("\ndeseja tentar novamente? [S/N]")

    if jogar =='S':
      jogar_uno()

  print("\n--- obrigado por jogar! até a próxima! ---")
  sys.exit()  # encerra o programa


# tudo começa aqui !
jogar_uno()
