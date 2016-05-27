__author__ = "Ignacio Alfonso Brito && Gabriel Garcia Buey"
from utils import if_
from random import randint

def memoize(heuristic):
    memo = {}
    def helper(state, player):
        inmmutable_state = (state.to_move, frozenset(state.board.items()))
        if inmmutable_state not in memo:
            memo[inmmutable_state] = heuristic(state, player)
        return memo[inmmutable_state]
    return helper

# stochastic heuristic
def h0(state, player):
    return randint(-100,100)

# brutal sadic stochastic heuristic
def h1(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    return randint(-100,100)

#MaqIAvel-4
@memoize
def h2(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    h = 0
    for (x, y) in state.moves:
        if x == 4:
            h -= 20
        elif x == 3 or x == 5:
            h -= 10
    for x in range(1, 8):
        for y in range(1, 7):
            if (x, y) not in state.board.keys():
                cv = chips_in_row((x, y), state.board, player, (0, 1))
                ch = chips_in_row((x, y), state.board, player, (1, 0))
                cds = chips_in_row((x, y), state.board, player, (1, -1))
                cdi = chips_in_row((x, y), state.board, player, (1, 1))
                h += ((100 * if_(cv > 1, cv, 0)) - (y * 2)) \
                    + (95 * if_(ch > 1, ch, 0)) \
                     + (((90* if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
                     + (((90 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))

                cv = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (0, 1))
                ch = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 0))
                cds = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, -1))
                cdi = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 1))
                h -= 1.5 * (((100 * if_(cv > 1, cv, 0)) - (y * 2))
                     + (95 * if_(ch > 1, ch, 0))
                     + (((90 * if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) 
                     + (((90 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1)))
    return h

# Nacho's DESTRUCTOR
@memoize
def h3(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    h = 0
    for x in state.moves:
        for b in range(1, 4):
            if x == (4, b):
                h -= 5
    for x in state.board:
        for a in range(1, 7):
            for a2 in range(3, 6):
                if (x == (a2, a)) & (state.board.get(x) == "X"):
                    h += 80
    return h

@memoize
def h4(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    h = 0
    for (x, y) in state.moves:
        if x == 4:
            h -= 20
        elif x == 3 or x == 5:
            h -= 10
        cv = chips_in_row((x, y), state.board, player, (0, 1))
        ch = chips_in_row((x, y), state.board, player, (1, 0))
        cds = chips_in_row((x, y), state.board, player, (1, -1))
        cdi = chips_in_row((x, y), state.board, player, (1, 1))
        h += ((90 * if_(cv > 1, cv, 0)) - (y * 2)) \
             + (100 * if_(ch > 1, ch, 0)) \
             + (((95 * if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
             + (((95 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))

        cv = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (0, 1))
        ch = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 0))
        cds = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, -1))
        cdi = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 1))
        h -= ((90 * if_(cv > 1, cv, 0)) - (y * 2)) \
            + (100 * if_(ch > 1, ch, 0)) \
            + (((95 * if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
            + (((95 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))

    return h

@memoize
def h5(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    h = 0
    for (x, y) in state.moves:
        h += y

        if x == 4:
            h -= 20
        elif x == 3 or x == 5:
            h -= 10
    for x in range(1, 8):
        for y in range(1, 7):
            if (x, y) not in state.board.keys():
                cv = chips_in_row((x, y), state.board, player, (0, 1))
                ch = chips_in_row((x, y), state.board, player, (1, 0))
                cds = chips_in_row((x, y), state.board, player, (1, -1))
                cdi = chips_in_row((x, y), state.board, player, (1, 1))
                h += ((100 * if_(cv > 1, cv, 0)) - (y * 2)) \
                     + (95 * if_(ch > 1, ch, 0)) \
                     + (((90 * if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
                     + (((90 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))

                cv = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (0, 1))
                ch = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 0))
                cds = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, -1))
                cdi = chips_in_row((x, y), state.board, if_(player == 'X', 'O', 'X'), (1, 1))
                h -= ((90 * if_(cv > 1, cv, 0)) - (y * 2)) \
                     + (100 * if_(ch > 1, ch, 0)) \
                     + (((95 * if_(cds > 1, cds, 0)) + (y * 2)) * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
                     + (((95 * if_(cdi > 1, cdi, 0)) + (y * 2)) * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))

    return h

#Nacho's Reaper 'Wall of death'
@memoize
def h6(state, player):
    he = 1000
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    for x in state.moves:
        for b in range(1, 4):
            if x == (4, b):
                he -= 100
    for x in state.board:
        for a in range(1, 7):
            for a2 in range(4, 6):
                if (x == (a2, a)) & (state.board.get(x) == player):
                    he += 20

    for a in range(1, 6):
        he1 = 0
        linea = 0
        for a1 in range(1, 7):
            if state.board.get((a1, a)) == if_(player == 'X', 'O', 'X'):
                if linea == 0:
                    linea = 1
                    he1 = 10
                else:
                    he1 = linea * 50
                    linea += 1
            else:
                linea = 0
            he -= he1
            he1 = 0

    for a in range(1, 7):
        he1 = 0
        linea = 0
        for a1 in range(1, 6):
            if state.board.get((a1, a)) == if_(player == 'X', 'O', 'X'):
                if linea == 0:
                    linea = 1
                    he1 = 10
                else:
                    he1 = linea * 50
                    linea += 1
            else:
                linea = 0
            he -= he1
            he1 = 0

    for a in range(1, 6):
        he1 = 0
        linea = 0
        for a1 in range(1, 7):
            if state.board.get((a1, a)) == player:
                if linea == 0:
                    linea = 1
                    he1 = 10
                else:
                    he1 = linea * 10
                    linea += 1
            else:
                linea = 0
            he += he1
            he1 = 0

    for a in range(1, 7):
        he1 = 0
        linea = 0
        for a1 in range(1, 6):
            if state.board.get((a1, a)) == player:
                if linea == 0:
                    linea = 1
                    he1 = 10
                else:
                    he1 = linea * 10
                    linea += 1
            else:
                linea = 0
            he += he1
            he1 = 0

    return he

#Tricker
@memoize
def h7(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)
    h = 0
    for (x, y) in state.moves:
        if x == 4:
            h -= 20
        elif x == 3 or x == 5:
            h -= 10

        if y == 1 or (x, y -1) in state.board:
            ch = chips_in_row((x, y + 1), state.board, player, (1, 0))
            cds = chips_in_row((x, y + 1), state.board, player, (1, -1))
            cdi = chips_in_row((x, y + 1), state.board, player, (1, 1))
            h += 1.15 * ((100 * if_(ch == 3, ch, 0))
                         + (((90 * if_(cds == 3, cds, 0)) + (y * 2))
                            * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1))
                         + (((90 * if_(cdi == 3, cdi, 0)) + (y * 2))
                            * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1)))

            ch = chips_in_row((x, y + 1), state.board, if_(player == 'X', 'O', 'X'), (1, 0))
            cds = chips_in_row((x, y + 1), state.board, if_(player == 'X', 'O', 'X'), (1, -1))
            cdi = chips_in_row((x, y + 1), state.board, if_(player == 'X', 'O', 'X'), (1, 1))
            h -= 100 * if_(ch == 3, ch, 0) + \
                 (((90 * if_(cds == 3, cds, 0)) + (y * 2))
                    * if_((x >= 5 & y in range(11 - x, 7)) or (x <= 3 & y in range(1, 5 - x)), 0, 1)) \
                + (((90 * if_(cdi == 3, cdi, 0)) + (y * 2))
                    * if_((x <= 3 & y in range(11 - x, 7)) or (x >= 5 & y in range(1, 5 - x)), 0, 1))
    return h

@memoize
def custom(state, player):
    if state.utility:
        return state.utility * if_(player == 'X', 10000, -10000)

    # External heuristic code goes here

    print("bleh")
    return 0


def chips_in_row((a, b), board, player, (delta_x, delta_y)):
    x, y = a, b
    n = 0
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = a, b
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1
    return n