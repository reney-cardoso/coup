import random
class Carta:
    def __init__(self, nome):
        self.nome = nome

class CartaPersonagem(Carta):
    def __init__(self, nome):
        super().__init__(nome)

class CartaReligiao(Carta):
    def __init__(self, nome):
        super().__init__(nome)

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []  # Lista de cartas em mãos
        self.moedas = 2
        self.bloqueado = False
        self.religiao = CartaReligiao("catolico")

#recursos de acoes livres
    def renda(self):
        self.moedas += 1

    def golpe(self, jogador_alvo):
        if self.moedas >= 7:
            self.moedas -= 7
            if jogador_alvo.cartas:
                carta_removida = random.choice(jogador_alvo.cartas)
                jogador_alvo.cartas.remove(carta_removida)
                print(f"{self.nome} aplicou um golpe em {jogador_alvo.nome}")
            else:
                print(f"{jogador_alvo.nome} não possui cartas para serem roubadas.")
        else:
            print(f"{self.nome} não tem moedas suficientes para aplicar o golpe (mínimo de 7 moedas).") 

    def ajuda_externa(self):
        if self.bloqueado:
            print("jogafor foi bloqueado pelo duque")
        else:
            self.moedas += 3

    def contestar(self, jogador_da_vez, nome_carta):
        if nome_carta in [carta.nome for carta in jogador_da_vez.cartas]:
            # O jogador da vez tem a carta, então o jogador que contestou perde uma carta
            if self.cartas:
                carta_removida = random.choice(self.cartas)
                self.cartas.remove(carta_removida)
            jogador_da_vez.bloqueado = False
        else:
            # O jogador da vez não tem a carta, então ele perde uma carta
            if jogador_da_vez.cartas:
                carta_removida = random.choice(jogador_da_vez.cartas)
                jogador_da_vez.cartas.remove(carta_removida)
            jogador_da_vez.bloqueado = True

    def bloquear(self,jogador_da_vez,nome_da_carta):
        self.nome_da_carta = nome_da_carta
        if self.bloqueado:     #se o jogador que esta bloqueando esta bloqueado
            jogador_da_vez.bloqueado = False
        else:
            jogador_da_vez.bloqueado = True # se nao for contestado e nao for bloqueado , entao bloqueia a acao do jogador da vez

    def desbloquear(self,jogador_da_vez):
        jogador_da_vez.bloqueado = True

#recursos das cartas de personagem
    def acao_assassino(self, jogador_alvo):
        if self.bloqueado:
            if self.moedas > 2:
                self.moedas-=3
                print("voce foi bloqueado pela condessa ou contestado")
            else:
                print("moedas insuficientes")
        else: #remocao da carta do jogador_alvo
            if self.moedas > 2:
                self.moedas -= 3
                carta_removida = random.choice(jogador_alvo.cartas)
                jogador_alvo.cartas.remove(carta_removida)
            else:
                print("moedas insuficientes")

    def acao_capitao(self, jogador_alvo):
        if self.bloqueado:
            print("voce foi bloqueado") #é bloqueado por um capitao ou por um embaixador
        else:
            if jogador_alvo.moedas > 0:
                if jogador_alvo.moedas > 1:
                    jogador_alvo.moedas -= 2
                    self.moedas += 2
                else:
                    jogador_alvo.moedas -= 1
                    self.moedas += 1
            else:
                print("jogador nao tem moedas")

    def acao_duque(self): #o duque tambem bloqueia a ajuda externa
        if self.bloqueado:
            print("voce foi contestado")
        else:
            self.moedas += 3

    def acao_condessa(self,jogador_alvo):
        if self.bloqueado:
            print("voce foi contestado")
        else:
            jogador_alvo.bloqueado = True

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

    def escol_cards_embaixador(self, jogo):
        print(f"escolha as cartas para remover:{self.cartas.nome[0]},{self.cartas.nome[1]},{self.cartas.nome[2]},{self.cartas.nome[3]}")

        ...
#recursos das cartas de religiao
    def pode_atacar(self, jogador_alvo):
        # Verifique se o jogador pode atacar o jogador_alvo
        # Considere a regra de não atacar jogadores com cartas de religião do mesmo tipo
        return self.religiao.nome != jogador_alvo.religiao.nome

    def converter_religiao(self, jogador_alvo, jogo):
        if self.moedas >= 2:
            self.moedas -= 2
            jogo.asilo += 2
            if self.religiao.nome == "catolico":
                jogador_alvo.religiao.nome = "protestante"
            else:
                jogador_alvo.religiao.nome = "catolico"
        else:
            print("Moedas insuficientes para converter religião.")

class Jogo:
    def __init__(self):
        self.jogadores = []  # Lista de jogadores
        self.baralho = []    # Lista de cartas no baralho
        self.asilo = 0       # Variável para armazenar as moedas do asilo
    def iniciar_jogo(self):
        # Distribuir cartas, definir ordem dos jogadores, etc.
        pass
    def acao_duque(self, jogador):

        jogador.pegar_moedas(self.asilo)
        self.asilo = 0
    def eliminar_jogador(self, jogador):
        # Remova o jogador da lista de jogadores
        pass
    def passar_vez(self):
        pass

