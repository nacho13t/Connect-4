import games
import heuristicas
from utils import if_
from random import randint

class Player:
    def __init__(self, chip):
        self.chip = chip

    def move(self, game, state):
        abstract

class Human(Player):
    def __init__(self, chip):
        Player.__init__(self, chip)

    def move(self, game, state):
        col_str = raw_input("Movimiento: ")
        coord = int(str(col_str).strip())
        x = coord
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
           if lm[0] == x:
               y = lm[1]
        return x, y

class Computer(Player):
    def __init__(self, chip, heuristic=1):
        Player.__init__(self, chip)
        strategies = (heuristicas.h0, heuristicas.h1, heuristicas.h6, heuristicas.h7, heuristicas.custom)
        self.heuristic = strategies[heuristic]

    def move(self, game, state):
        print "Thinking..."
        # return games.minimax_decision(state, game)
        # return games.alphabeta_full_search(state, game)
        return games.alphabeta_search(state, game, eval_fn=self.heuristic)

def play(initialPlayer, player1, player2):
    # game = games.TicTacToe(h=3,v=3,k=3)
    game = games.ConnectFour()
    game.initial.to_move = initialPlayer
    state = game.initial
    player = initialPlayer

    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        if player == player1.chip:
            move = player1.move(game, state)
            state = game.make_move(move, state)
            player = player2.chip
        else:
            move = player2.move(game, state)
            state = game.make_move(move, state)
            player = player1.chip
        print "\n-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "\r\n                            Final de la partida" \
                "\r\n                                 Winner:", \
                if_(state.utility,
                    if_(player == 'O', 'X', 'O'), if_(not state.moves, '-', if_(player == 'O', 'X', 'O')))
            break

def human_vs_computer():
    player_start = True
    while True:
        player_start = raw_input("Do you want to start? [y/n]: ")
        if player_start == 'y':
            player_start = True
            break
        elif player_start == 'n':
            player_start = False
            break
        print("Please answer with 'y' or 'n'")
    computer_chip = 'O'
    player_chip = 'X'
    while True:
        player_chip = raw_input("Do you want to be X or O ? : ")
        if player_chip == 'O':
            computer_chip = 'X'
            break
        elif player_chip == 'X': break
        print("Please enter 'X' or 'O'")
    difficulty = 1
    while True:
        print("1. Regalado\r\n2. Easy\r\n3. Medium\r\n4. I don't want to win (and you won't)\r\n5. Custom")
        try:
            difficulty = int(raw_input("Select AI difficulty: "))
            if difficulty > 0 and difficulty < 6: break
            print("Invalid difficulty")
        except ValueError:
            print("Please enter a number [1-5]\r\n")

    player = Human(player_chip)
    computer = Computer(computer_chip, difficulty - 1)
    play(if_(player_start, player_chip, computer_chip), player, computer)

def computer_vs_computer():
    difficulty1 = 1
    difficulty2 = 1
    print("1. Regalado\r\n2. Easy\r\n3. Medium\r\n4. Hard\r\n5. Custom")
    while True:
        try:
            difficulty1 = int(raw_input("Select Computer1 difficulty: "))
            if difficulty1 > 0 and difficulty1 < 6: break
            print("Invalid difficulty")
        except ValueError:
            print("Please enter a number [1-5]\r\n")
    while True:
        try:
            difficulty2 = int(raw_input("Select Computer2 difficulty: "))
            if difficulty2 > 0 and difficulty2 < 6: break
            print("Invalid difficulty")
        except ValueError:
            print("Please enter a number [1-5]\r\n")
    computer1_start = True
    while True:
        computer1_start = raw_input("Wich one should start Computer1 or Computer2 ? : ")
        if computer1_start == '1':
            computer1_start = True
            break
        elif computer1_start == '2':
            computer1_start = False
            break
        print("Please answer with '1' or '2'")
    computer1_chip = 'X'
    computer2_chip = 'O'
    while True:
        computer1_chip = raw_input("Assign Computer1 X or O "
                                "(the remainig one will be automatically assigned to Computer2): ")
        if computer1_chip == 'O':
            computer2_chip = 'X'
            break
        elif computer1_chip == 'X':
            break
        print("Please enter 'X' or 'O'")
    computer1 = Computer(computer1_chip, difficulty1 - 1)
    computer2 = Computer(computer2_chip, difficulty2 - 1)
    play(if_(computer1_start, computer1_chip, computer2_chip), computer1, computer2)

def human_vs_human():
    player1_start = True
    while True:
        player1_start = raw_input("Wich one should start Player1 or Player2 ? [Enter '0' for random selection]: ")
        if player1_start == '1':
            player1_start = True
            break
        elif player1_start == '2':
            player1_start = False
            break
        elif player1_start == '0':
            player1_start = randint(0, 2)
            if player1_start == 0: player1_start = True
            else: player1_start = False
            if player1_start: print "Player1 start"
            else: print "Player2 start"
            break
        print("Please answer with '0', '1' or '2'")
    player1_chip = 'X'
    player2_chip = 'O'
    while True:
        player1_chip = raw_input("Assign Player1 X or O "
                                 "(the remainig one will be automatically assigned to Player2)"
                                 " [Enter '0' for random selection]: ")
        if player1_chip == 'O':
            player2_chip = 'X'
            break
        elif player1_chip == 'X':
            break
        elif player1_chip == '0':
            player1_chip = randint(0, 2)
            if player1_chip == 0: player1_chip = 'X'
            else: player1_chip = 'O'
            print "Player1 is ", player1_chip
            break
        print("Please enter 'X' or 'O' or '0'")
    player1 = Human(player1_chip)
    player2 = Human(player2_chip)
    play(if_(player1_start, player1_chip, player2_chip), player1, player2)

while True:
    operations = (human_vs_computer, computer_vs_computer, human_vs_human)
    option = 5
    print "                            CONNECT - 4\r\n                            FSI EDITION" \
          "\r\n1. Human VS Computer\r\n2. Computer VS Computer\r\n3. Human VS Human\r\n4. Exit"
    while True:
        try:
            option = int(raw_input("Select operation: "))
            if option > 0 and option < 5: break
            print("Invalid mode!")
        except ValueError:
            print("Please introduce a number! [1-4]")
    if (option - 1) == 3: break
    operations[option - 1]()