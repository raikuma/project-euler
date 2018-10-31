from random import randint, shuffle

DEBUG = False

def dice():
    return randint(1, 4)

board = {}
for i in range(40):
    board[i] = 0

CC = [2, 17, 33]
CH = [7, 22, 36]
R = [5, 15, 25, 35]
U = [12, 28]

GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5
G2J = 30
def nextR():
    p = player
    while p not in R:
        p = (p + 1) % 40
    return p
def nextU():
    p = player
    while p not in U:
        p = (p + 1) % 40
    return p
def back3():
    return (player - 3) % 40
def stay():
    return player

card = list(range(16))
shuffle(card)
card_idx = 0
card_eff = {0:GO, 1:JAIL,
            2:GO, 3:JAIL, 4:C1, 5:E3, 6:H2, 7:R1,
            8:nextR, 9:nextR, 10:nextU, 11:back3,
            12:stay, 13:stay, 14:stay, 15:stay}
def draw():
    global card_idx
    c = card[card_idx]
    card_idx = (card_idx + 1) % 16
    return card_eff[c]

db_cnt = 0
player = GO
board[GO] += 1

if DEBUG:
    print('[Start Game]')
for i in range(1000000):
    d1, d2 = dice(), dice()
    if DEBUG:
        print('[Dice Roll] {}, {}'.format(d1, d2))
    if d1 == d2:
        db_cnt += 1
        if DEBUG:
            print('[Double!] {}/3'.format(db_cnt))
    else:
        db_cnt = 0
    player = (player + d1 + d2) % 40
    go = player
    if db_cnt == 3:
        if DEBUG:
            print('[3 Double. Go to JAIL]')
        go = JAIL
    elif go in CC or go in CH:
        eff = draw()
        if DEBUG:
            print('[Draw Card] {}'.format(eff))
        if type(eff) == int:
            go = eff
        else:
            go = eff()
    player = go
    if player == G2J:
        if DEBUG:
            print('[Go to JAIL]')
        player = JAIL
    if DEBUG:
        print('[Move to] {}'.format(go))
    board[player] += 1

res = sorted(board.items(), key=lambda x:x[1], reverse=True)
print(res)