'''continue esse codigo e implemente o metodo acao_embaixador que consiste em remover 2 cartas
do atributo baralho da classe Jogo e adicionar essas duas cartas a lista do atributo cartas da classe jogador, 
depois o jogador escolhe 2 cartas da classe jogador e as remove da lista desse atributo, e adiciona as mesmas 
ao atributo baralho da classe jogo.

import random
class Carta:
    def __init__(self, nome):
        self.nome = nome

class CartaPersonagem(Carta):
    def __init__(self, nome):
        super().__init__(nome)

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []  # Lista de cartas em mãos
        self.moedas = 2
        self.bloqueado = False

    def acao_embaixador(self, jogo):
        if self.bloqueado:
            print("Você foi contestado.")
        else:
            # Remover 2 cartas do baralho do jogo
            for _ in range(2):
                carta_removida = jogo.baralho.pop()
                # Adicionar a carta à lista de cartas do jogador
                self.cartas.append(carta_removida)

            # O jogador escolhe 2 cartas para devolver ao baralho do jogo
            # (implemente a lógica para o jogador escolher as cartas)

class Jogo:
    def __init__(self):
        self.jogadores = []  # Lista de jogadores
        self.baralho = []    # Lista de cartas no baralho
        self.asilo = 0       # Variável para armazenar as moedas do asilo
    def iniciar_jogo(self):
        # Distribuir cartas, definir ordem dos jogadores, etc.
        pass'''

cartas = ['Ás', 'Rei', 'Dama', 'Valete']

# Solicita ao jogador que escolha 2 cartas
carta1 = input(f"Escolha a primeira carta ({cartas[0]}, {cartas[1]}, {cartas[2]}, {cartas[3]}): ")
carta2 = input(f"Escolha a segunda carta ({cartas[0]}, {cartas[1]}, {cartas[2]}, {cartas[3]}): ")

# Verifica se as cartas escolhidas estão na lista
if carta1 in cartas and carta2 in cartas:
    # Remove as cartas escolhidas da lista
    cartas.remove(carta1)
    cartas.remove(carta2)

print("Cartas restantes na lista:", cartas)