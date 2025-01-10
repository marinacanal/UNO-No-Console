# Jogo de Uno em Python

## Sobre o Projeto
Este projeto consiste em um jogo de Uno simples implementado em Python. Criado por mim (**Marina Canal**) e **Luiz Gustavo** para a disciplina de Ciência da Computação (Noturno) da UFFS - Campus Chapecó, o jogo simula partidas de Uno para 1 a 4 jogadores, utilizando um baralho personalizado e regras simplificadas.

## Como Funciona
O jogo permite que os jogadores:
- Pesquem cartas do baralho.
- Joguem cartas que combinem em cor ou número com a carta na mesa.
- Vejam suas cartas na mão, com cores destacadas para facilitar a identificação.
- Ganhem a partida ao esvaziarem sua mão.

Se o baralho acabar e nenhum jogador tiver esvaziado a mão, o jogo termina em empate.

## Requisitos
- Python 3.x

## Como Rodar o Jogo
1. Certifique-se de ter o Python instalado em seu sistema.
2. Faça o download ou clone o repositório contendo o arquivo `uno.py`.
3. Abra um terminal na pasta onde o arquivo está localizado.
4. Execute o seguinte comando:
   ```bash
   python uno.py
   ```
5. Siga as instruções no terminal para iniciar e jogar o jogo.

## Regras do Jogo
1. Cada jogador começa com 5 cartas.
2. Apenas cartas da mesma cor ou número podem ser jogadas na mesa.
3. Caso o jogador não tenha cartas válidas para jogar, ele pode pescar do baralho.
4. O jogador que ficar sem cartas primeiro vence a partida.
5. Se o baralho acabar antes que alguém vença, o jogo termina em empate.

## Controles e Comandos
- Durante o jogo, os jogadores verão suas cartas listadas com um número correspondente.
- Para jogar uma carta, digite o número da carta.
- Para pescar uma carta do baralho, digite `P`.

## Estrutura do Código
- **Funções principais:**
  - `criar_baralho()`: Cria o baralho com cores e números personalizados.
  - `embaralhar_baralho(baralho)`: Embaralha o baralho.
  - `distribuir_cartas(quantidade_jogadores, jogadores, baralho)`: Distribui as cartas entre os jogadores.
  - `pescar_ou_jogar_carta(baralho, pilha_mesa, carta_na_mesa, jogador, maos)`: Lida com a jogada ou pesca de carta do jogador.
  - `terminar_jogo(jogador)`: Exibe a tela de vitória ou empate e pergunta se o jogador deseja reiniciar.
  - `jogar_uno()`: Controla o fluxo principal do jogo.

## Créditos
- **Autores:** Marina Canal e Luiz Gustavo
- **Universidade:** Universidade Federal da Fronteira Sul (UFFS) - Campus Chapecó

## Observações
Este projeto foi desenvolvido para fins acadêmicos e como uma introdução prática à programação em Python. O jogo pode ser estendido com regras adicionais ou melhorado para incluir uma interface gráfica no futuro.

Divirta-se jogando Uno! 

