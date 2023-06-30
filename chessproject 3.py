import copy


class Board:
    def __init__(self):
        self.board = [[lb, hb, cb, qb, kb, cb, hb, lb],
                      [pb, pb, pb, pb, pb, pb, pb, pb],
                      [dot, dot, dot, dot, dot, dot, dot, dot],
                      [dot, dot, dot, dot, dot, dot, dot, dot],
                      [dot, dot, dot, dot, dot, dot, dot, dot],
                      [dot, dot, dot, dot, dot, dot, dot, dot],
                      [pw, pw, pw, pw, pw, pw, pw, pw],
                      [lw, hw, cw, qw, kw, cw, hw, lw]]

        copy_board = copy.deepcopy(self.board)
        self.reboard = [copy_board]

    def BoardOfp(self):
        print('-' * 35)
        for i in t.board:
            for j in i:
                print(j, end='   ')
            print()
            # print(j,end= ' ')
        print('-' * 35)

    def cheker(self, y, x, y1, x1):
        if t.board[y1][x1].colour == -10 or abs(t.board[y1][x1].colour - t.board[y][x].colour) == 1:
            winc = self.board[y][x].cheker(y, x, y1, x1)
            return winc
        else:
            return False

    def beatofcan(self, y, x):
        winc_can = False
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.cheker(v, k, y, x):
                    winc_can = True
        return winc_can

    def EZFV(self, y, x):
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.cheker(v, k, y, x):
                    return (v, k)

    def echis(self, y, x):
        moves = []
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.cheker(y, x, v, k) and not t.can_move(y, x, v, k):
                    moves.append((v, k))
        return moves

    def can_move(self, y, x, y1, x1):
        q = kw if t.board[y][x].colour == 1 else kb
        if t.board[y][x].__class__ != King:
            if t.beatofcan(q.y, q.x):
                save = t.board[y1][x1]
                t.board[y1][x1] = dot
                winc = t.beatofcan(q.y, q.x)
                t.board[y1][x1] = save
            else:
                save = t.board[y][x]
                save1 = t.board[y1][x1]
                t.board[y1][x1] = t.board[y][x]
                t.board[y][x] = dot
                winc = t.beatofcan(q.y, q.x)
                t.board[y][x] = save
                t.board[y1][x1] = save1
            return winc
        else:
            save = t.board[y1][x1]
            t.board[y1][x1] = q
            winc = t.beatofcan(y1, x1)
            t.board[y1][x1] = save
            return winc

    def mat(self):
        winc_mat1 = True
        winc_mat2 = []
        for v, i in enumerate(t.board):
            for k, j in enumerate(i):
                if t.cheker(v, k, kw.y, kw.x) or t.cheker(v, k, kb.y, kb.x):
                    q = kw if t.board[v][k].colour == 0 else kb
                    if self.beatofcan(v, k) and not self.can_move(self.EZFV(v, k)[0], self.EZFV(v, k)[1], v, k):
                        winc_mat1 = True
                    else:
                        winc_mat1 = False
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            try:
                                if t.cheker(q.y, q.x, q.y + i, q.x + j):
                                    save = t.board[q.y + i][q.x + j]
                                    ultra_save = t.board[q.y][q.x]
                                    t.board[q.y][q.x] = dot
                                    t.board[q.y + i][q.x + j] = q
                                    if t.beatofcan(q.y + i, q.x + j):
                                        t.board[q.y + i][q.x + j] = save
                                        t.board[q.y][q.x] = ultra_save
                                        winc_mat2.append(False)
                                    else:
                                        t.board[q.y + i][q.x + j] = save
                                        t.board[q.y][q.x] = ultra_save
                                        winc_mat2.append(True)
                                else:
                                    winc_mat2.append(False)
                            except:
                                winc_mat2.append(False)
                                continue
        if True in winc_mat2:
            winc_mat2 = True
        else:
            winc_mat2 = False
        return winc_mat1 + winc_mat2

    def sh_mat(self):
        count_sw = []
        count_sb = []
        for i in t.board:
            for j in i:
                if j == sw:
                    count_sw.append('1')
                elif j == sb:
                    count_sb.append('1')
        if len(count_sw) == 0 or len(count_sb) == 0:
            return False
        else:
            return True

    def shbeatofcan(self, y, x, y1, x1):
        winc = self.board[y][x].shbeatofcan(y, x, y1, x1)
        return winc

    def shcan_move(self, y, x, y1, x1):
        return t.board[y][x].shcan_move(y, x, y1, x1)

    def check_next(self, y, x):
        can_move = []
        moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
        for i in range(0, 4):
            try:
                y1 = y + moves[i][0]
                x1 = x + moves[i][1]
                if self.shbeatofcan(y, x, y1, x1)[0]:
                    can_move.append((y + moves[i][0], x + moves[i][1]))
            except:
                continue
        return can_move

    def sh_into_shq(self):
        for v, i in enumerate(t.board[0]):
            if i == sw:
                t.board[0][v] = sqw
                t.BoardOfp()
        for v, i in enumerate(t.board[7]):
            if i == sb:
                t.board[7][v] = sqb
                t.BoardOfp()


class NoneType:
    def __init__(self):
        self.colour = -10

    def __repr__(self):
        return '▢'

    def cheker(self, y, x, y1, x1):
        return False

    def shbeatofcan(self, y, x, y1, x1):
        return (False, 0, 0)

    def shcan_move(self, y, x, y1, x1):
        return False


class ChessFigure():
    IMG = None

    def __init__(self, colour, y=None, x=None):
        self.colour = colour
        self.y = y
        self.x = x

    def __repr__(self):
        return self.IMG[1 if self.colour else 0]


class Pawn(ChessFigure):
    point = 0

    IMG = ('♙', '♟')

    def cheker(self, y, x, y1, x1):
        if self.colour == 1:
            colourp = 1
            y_factor = y1 + 1
        else:
            colourp = -1
            y_factor = y1 - 1
        if y1 < 0 or y1 > 7:
            winc = False
        elif x1 < 0 or x1 > 7:
            winc = False
        else:
            if t.board[y1][x1].colour == -10:
                if (y == 6 or y == 1):
                    if x == x1 and 0 < (y - y1) * colourp < 3 and t.board[y_factor][x1].colour == -10:
                        winc = True
                    elif x == x1 and (y - y1) * colourp == 1:
                        winc = True
                    else:
                        winc = False
                else:
                    if x == x1 and (y - y1) * colourp == 1:
                        winc = True
                    else:
                        winc = False
            elif abs(t.board[y1][x1].colour - t.board[y][x].colour) == 1:
                if abs(x - x1) == 1 and (y - y1) * colourp == 1:
                    winc = True
                else:
                    winc = False
            else:
                winc = False
        return winc


class King(ChessFigure):
    IMG = ('♔', '♚')

    def cheker(self, y, x, y1, x1):
        if (abs(x1 - x) == 1 and abs(y1 - y) == 1):
            winc = True
        elif (abs(x1 - x) == 0 and abs(y1 - y) == 1):
            winc = True
        elif (abs(x1 - x) == 1 and abs(y1 - y) == 0):
            winc = True
        else:
            winc = False

        q = kw if self.colour == 0 else kb
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if t.board[y1 + i][x1 + j] == q:
                        winc = False
                except:
                    continue
        return winc


class Quinn(ChessFigure):
    IMG = ('♕', '♛')

    def cheker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = lw if q == qw else lb
        v = cw if q == qw else cb
        if x == x1 or y == y1:
            return c.cheker(y, x, y1, x1)
        elif (y != y1 and x != x1) or (x != x1 and y != y1):
            return v.cheker(y, x, y1, x1)
        else:
            return False


class Ladya(ChessFigure):
    IMG = ('♖', '♜')

    def cheker(self, y, x, y1, x1):
        winc = True
        if y == y1 and x != x1:
            q = x if x1 > x else x1
            e = x1 if x1 > x else x
            for i in t.board[y][q + 1:e]:
                if i != dot:
                    winc = False
        elif x == x1 and y != y1:
            q = y1 if y > y1 else y
            e = y if y > y1 else y1
            for i in t.board[q + 1:e]:
                if i[x] != dot:
                    winc = False
        else:
            winc = False
        return winc


class Horse(ChessFigure):
    IMG = ('♘', '♞')

    def cheker(self, y, x, y1, x1):
        if abs(y - y1) == 2 and abs(x - x1) == 1:
            winc = True
        elif abs(x - x1) == 2 and abs(y - y1) == 1:
            winc = True
        else:
            winc = False
        return winc


class Bishop(ChessFigure):
    IMG = ('♗', '♝')

    def cheker(self, y, x, y1, x1):
        winc = True
        if x == x1 or y == y1:
            winc = False
        elif x + y == x1 + y1:
            q = x1 if x1 > x and y > y1 else x
            c = y1 if x1 > x and y > y1 else y
            v = y if x1 > x and y > y1 else y1
            for i in t.board[c + 1:v]:
                if i[q - 1] != dot:
                    winc = False
                q -= 1
        elif x + y1 == y + x1:
            q = x if x1 > x and y1 > y else x1
            c = y if x1 > x and y1 > y else y1
            v = y1 if x1 > x and y1 > y else y
            for i in t.board[c + 1:v]:
                if i[q + 1] != dot:
                    winc = False
                q += 1
        else:
            winc = False
        return winc


class LHorse(ChessFigure):
    IMG = ('♖♘', '♜♞')

    def cheker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = lw if q == qw else lb
        v = hw if q == qw else hb
        if (y == y1 and x != x1) or (x == x1 and y != y1):
            return c.cheker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (abs(x - x1) == 2 and abs(y - y1) == 1):
            return v.cheker(y, x, y1, x1)
        else:
            return False


class BHorse(ChessFigure):
    IMG = ('♗♘', '♝♞')

    def cheker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = cw if q == qw else cb
        v = hw if q == qw else hb
        if (x + y == x1 + y1) or (x + y1 == y + x1):
            return c.cheker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (abs(x - x1) == 2 and abs(y - y1) == 1):
            return v.cheker(y, x, y1, x1)
        else:
            return False


class QHorse(ChessFigure):
    IMG = ('♕♘', '♛♞')

    def cheker(self, y, x, y1, x1):
        q = qb if self.colour == 0 else qw
        c = qw if q == qw else qb
        v = hw if q == qw else hb
        if x == x1 or y == y1 or (x + y == x1 + y1) or (x + y1 == y + x1):
            return c.cheker(y, x, y1, x1)
        elif (abs(y - y1) == 2 and abs(x - x1) == 1) or (abs(x - x1) == 2 and abs(y - y1) == 1):
            return v.cheker(y, x, y1, x1)
        else:
            return False


class Shashka(ChessFigure):
    IMG = ('⛀', '⛂')

    def shbeatofcan(self, y, x, y1, x1):
        if y == y1 or x == x1:
            winc = False
            q, w = None, None
        elif abs(y - y1) == 2 and abs(x - x1) == 2 and t.board[y1][x1] == dot:
            z = 0 if t.board[y][x].colour == 1 else 1
            if y1 > y and x1 > x:
                winc = True if t.board[y + 1][x + 1].colour == z else False
                q, w = 1, 1
            elif y1 > y and x > x1:
                winc = True if t.board[y + 1][x - 1].colour == z else False
                q, w = 1, -1
            elif y > y1 and x1 > x:
                winc = True if t.board[y - 1][x + 1].colour == z else False
                q, w = -1, 1
            else:
                winc = True if t.board[y - 1][x - 1].colour == z else False
                q, w = -1, -1
        else:
            winc = False
            q, w = None, None
        return (winc, q, w)

    def shcan_move(self, y, x, y1, x1):
        q = -1 if t.board[y][x].colour == 1 else 1
        if y1 == y + q and abs(x - x1) == 1 and t.board[y1][x1].colour == -10:
            return True
        else:
            return False


class SHQueen(ChessFigure):
    IMG = ('⛁', '⛃')

    def shcan_move(self, y, x, y1, x1):
        q = cw if t.board[y][x].colour == 1 else cb
        return q.cheker(y, x, y1, x1)

    def shbeatofcan(self, y, x, y1, x1):
        return True


def recoil_board():
    while True:
        q = input(f'Enter how many moves you want to roll back the game (max : {len(t.reboard) - 1}): ')
        try:
            q = int(q)
        except:
            recoil_board()
        else:
            if 0 < q <= len(t.reboard) - 1:
                return (t.reboard[-(q + 1)], q)
            else:
                recoil_board()


def input_cord(a):
    while True:
        q = input(a)
        try:
            q = int(q)
        except:
            print('Data entered incorrectly')
        else:
            q = str(q)
            q = '0' + q if len(q) == 1 else q
            if len(q) == 2 and 0 <= int(q) <= 77:
                return q
            else:
                print('Data entered incorrectly')


dot = NoneType()
pb = Pawn(0)
pw = Pawn(1)
kb = King(0, 0, 4)
kw = King(1, 7, 4)
qb = Quinn(0)
qw = Quinn(1)
lb = Ladya(0)
lw = Ladya(1)
hb = Horse(0)
hw = Horse(1)
cb = Bishop(0)
cw = Bishop(1)
qhw = QHorse(1)
qhb = QHorse(0)
lhb = LHorse(0)
lhw = LHorse(1)
chb = BHorse(0)
chw = BHorse(1)
sw = Shashka(1)
sb = Shashka(0)
sqw = SHQueen(1)
sqb = SHQueen(0)
t = Board()
i = 1
clr = ('black', 'white')
game = input('(Chess : 1, Checkers : 2) : ')
if game == '1':
    while t.mat():
        vvod = input('Enter what you want to do (Move : 1, Rollback : 2, View moves : 3): ')
        t.BoardOfp()
        if vvod == '1':
            print(f'Ходят {clr[i % 2]}')
            cord1 = input_cord('Enter the coordinates of the figure you want to resemble: ')
            cord2 = input_cord('Enter where you want to go: ')
            y = int(cord1[0])
            x = int(cord1[1])
            y1 = int(cord2[0])
            x1 = int(cord2[1])
            if t.board[y][x].colour == i % 2:
                if (t.cheker(y, x, y1, x1) and not t.can_move(y, x, y1, x1)):
                    if t.board[y][x].__class__ == King:
                        t.board[y][x].y = y1
                        t.board[y][x].x = x1
                    t.board[y][x], t.board[y1][x1] = dot, t.board[y][x]
                    copy_board1 = copy.deepcopy(t.board)
                    t.reboard.append(copy_board1)
                    t.BoardOfp()
                    print('\n' * 3)
                    if t.beatofcan(kw.y, kw.x):
                        print('Check to the white king')
                    elif t.beatofcan(kb.y, kb.x):
                        print('Check to the black king')
                else:
                    print()
                    print('Wrong move, try something else')
                    continue
            else:
                print('\n' * 3)
                print('You must walk in a different color')
                continue
            i += 1
        elif vvod == '2':
            a, s = recoil_board()
            a = copy.deepcopy(a)
            t.board = a
            t.BoardOfp()
            i -= s
            t.reboard = t.reboard[:len(t.reboard) - s]
        elif vvod == '3':
            codr1, cord2 = input_cord('Enter the moves of which piece you want to see: ')
            codr1 = int(codr1)
            cord2 = int(cord2)
            for i, v in t.echis(codr1, cord2):
                if t.board[i][v].__class__ != NoneType:
                    t.board[i][v] = f'({t.board[i][v]})'
                else:
                    t.board[i][v] = '■'
            t.BoardOfp()
            a = copy.deepcopy(t.reboard[-1])
            t.board = a
            # t.board
        else:
            continue
    else:
        print(f'Game over, win {clr[(i - 1) % 2]}')
        t.BoardOfp()
if game == '2':
    t.board = [[dot, sb, dot, sb, dot, sb, dot, sb],
               [sb, dot, sb, dot, sb, dot, sb, dot],
               [dot, sb, dot, sb, dot, sb, dot, sb],
               [dot, dot, dot, dot, dot, dot, dot, dot],
               [dot, dot, dot, dot, dot, dot, dot, dot],
               [sw, dot, sw, dot, sw, dot, sw, dot],
               [dot, sw, dot, sw, dot, sw, dot, sw],
               [sw, dot, sw, dot, sw, dot, sw, dot]]


    while t.sh_mat():
        t.BoardOfp()
        print(f'Ходят {clr[i % 2]}')
        cord1 = input_cord('Enter the coordinates of the figure you want to resemble: ')
        cord2 = input_cord('Enter where you want to go: ')
        y = int(cord1[0])
        x = int(cord1[1])
        y1 = int(cord2[0])
        x1 = int(cord2[1])
        if t.board[y][x].colour == i % 2:
            if t.check_next(y, x):
                while t.check_next(y, x):
                    y1, x1 = t.check_next(y, x)[0][0], t.check_next(y, x)[0][1]
                    q = t.shbeatofcan(y, x, y1, x1)[1]
                    w = t.shbeatofcan(y, x, y1, x1)[2]
                    t.board[y][x], t.board[y1][x1] = dot, t.board[y][x]
                    t.board[y + q][x + w] = dot
                    y, x = y1, x1
                    t.sh_into_shq()
                    t.BoardOfp()
                i += 1
            elif t.shcan_move(y, x, y1, x1):
                t.board[y][x], t.board[y1][x1] = dot, t.board[y][x]
                t.sh_into_shq()
                i += 1
            else:
                print('Wrong move1')
                continue
        else:
            print('Wrong move2')
            continue
    else:
        print(f'Game over, win {clr[(i - 1) % 2]}')
        t.BoardOfp()