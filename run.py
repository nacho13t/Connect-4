import games
import heuristicas
#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial


player = 'X'

while True:  #pide y genera accion
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':  #tu
        move = games.alphabeta_search(state, game, eval_fn=heuristicas.h7)
        #col_str = raw_input("Movimiento: ")
        #coor = int(str(col_str).strip())
        #x = coor
        #y = -1
        #legal_moves = game.legal_moves(state)
        #for lm in legal_moves:
        #    if lm[0] == x:
        #        y = lm[1]

        state = game.make_move(move, state)
        #state = game.make_move((x, y), state)
        player = 'X'
    else:  #maquina
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, eval_fn=heuristicas.h6)

        state = game.make_move(move, state)
        player = 'O'
    print "\n-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
