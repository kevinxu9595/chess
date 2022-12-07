import pygame
import time

pygame.init()
pygame.display.set_caption("Kevin's Chess Program")
programIcon = pygame.image.load('knight_black.png')
pygame.display.set_icon(programIcon)

# defines the width and height of the display
display_width = 1280
display_height = 720

# defines block width and height
block_height = 80
block_width = 80

# defines colours
white = (250, 250, 250)
black = (5, 5, 5)
light = (237, 217, 184)
dark = (60, 40, 30)
teal = (0, 127, 127)
red = (200, 0, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
clock = pygame.time.Clock()


def initialize_piece(pieces):
    for i in range(len(pieces)):
        img = None
        if pieces[i].abbr == "P" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("pawn_white.png")
            else:
                img = pygame.image.load("pawn_black.png")
        elif pieces[i].abbr == "Q" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("queen_white.png")
            else:
                img = pygame.image.load("queen_black.png")
        elif pieces[i].abbr == "B" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("bishop_white.png")
            else:
                img = pygame.image.load("bishop_black.png")
        elif pieces[i].abbr == "R" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("rook_white.png")
            else:
                img = pygame.image.load("rook_black.png")
        elif pieces[i].abbr == "N" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("knight_white.png")
            else:
                img = pygame.image.load("knight_black.png")
        elif pieces[i].abbr == "K" and not pieces[i].taken:
            if pieces[i].colour == "White":
                img = pygame.image.load("king_white.png")
            else:
                img = pygame.image.load("king_black.png")
        if img != None:
            game_display.blit(img, (pieces[i].x * 80 - 40, pieces[i].y * -80 + 650))


def initialize_taken(move_font, my_font, pieces):
    img_list = ["pawn_white.png", "knight_white.png", "bishop_white.png", "rook_white.png", "queen_white.png",
                "pawn_black.png", "knight_black.png", "bishop_black.png", "rook_black.png", "queen_black.png"]
    piece_list = ["P", "N", "B", "R", "Q"]
    for i in range(5):
        dead_white = 0
        dead_black = 0
        for j in pieces:
            if j.abbr == piece_list[i] and j.taken:
                if j.colour == "White":
                    dead_white += 1
                else:
                    dead_black += 1
        game_display.blit(pygame.transform.scale(pygame.image.load(img_list[i]), (36, 36)), (i * 42 + 705, 510))
        test = move_font.render(str(dead_white), 1, white)
        game_display.blit(test, (i * 42 + 720, 550))
        game_display.blit(pygame.transform.scale(pygame.image.load(img_list[i + 5]), (36, 36)), (i * 42 + 705, 570))
        test = move_font.render(str(dead_black), 1, white)
        game_display.blit(test, (i * 42 + 720, 610))
    test = my_font.render("Pieces taken", 1, white)
    game_display.blit(test, (710, 635))


def initialise_circle(selected):
    moves = selected.legal
    for i in moves:
        img = pygame.image.load("dot.png")
        game_display.blit(img, ((i[0]) * 80 + 60, ((6 - i[1]) * 80 + 110)))


########################################################################################################################

class Piece:
    def __init__(self, x, y, colour, abbr):
        self.x = x
        self.y = y
        self.colour = colour
        self.abbr = abbr
        self.taken = False
        self.in_check = False
        self.legal = []


def setup(pieces1, pieces2):
    array = []
    row = []
    for i in range(8):
        row.append(" ")
    for i in range(8):
        array.append(list(row))
    for i in pieces1:
        if not i.taken:
            array[i.y - 1][i.x - 1] = i.abbr
    for i in pieces2:
        if not i.taken:
            array[i.y - 1][i.x - 1] = i.abbr.lower()
    return array


def valid(piece, x, y, array):
    moves = []
    if piece.lower() == "n":
        potential_moves = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1], [x - 2, y - 1],
                           [x - 1, y - 2],
                           [x + 1, y - 2], [x + 2, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        if piece == "N":
            for i in moving:
                if array[i[1]][i[0]] not in "XPNBRQK":
                    if array[i[1]][i[0]] == " ":
                        moves.append(i)
                    else:
                        temp = i
                        temp.append(array[i[1]][i[0]])
                        moves.append(temp)
        elif piece == "n":
            for i in moving:
                if array[i[1]][i[0]] not in "Xpnbrqk":
                    if array[i[1]][i[0]] == " ":
                        moves.append(i)
                    else:
                        temp = i
                        temp.append(array[i[1]][i[0]])
                        moves.append(temp)

    elif piece.lower() == "k":
        potential_moves = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1],
                           [x, y - 1], [x + 1, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        if piece == "K":
            for i in moving:
                if array[i[1]][i[0]] not in "XPNBRQK":
                    if array[i[1]][i[0]] == " ":
                        moves.append(i)
                    else:
                        temp = i
                        temp.append(array[i[1]][i[0]])
                        moves.append(temp)
        elif piece == "k":
            for i in moving:
                if array[i[1]][i[0]] not in "Xpnbrqk":
                    if array[i[1]][i[0]] == " ":
                        moves.append(i)
                    else:
                        temp = i
                        temp.append(array[i[1]][i[0]])
                        moves.append(temp)

    elif piece == "P":
        if y == 1:
            moving = [[x, y + 1], [x, y + 2]]
        else:
            moving = [[x, y + 1]]
        for i in moving:
            if array[i[1]][i[0]] not in "XPNBRQKpnbrqk":
                moves.append(i)
            else:
                break

    elif piece == "p":
        if y == 6:
            moving = [[x, y - 1], [x, y - 2]]
        else:
            moving = [[x, y - 1]]
        for i in moving:
            if array[i[1]][i[0]] not in "XPNBRQKpnbrqk":
                moves.append(i)
            else:
                break

    elif piece == "R" or piece == "Q":
        for i in range(1, 8 - x):
            if array[y][x + i] == " ":
                moves.append([x + i, y])
            else:
                if array[y][x + i] in "pnbrqk":
                    moves.append([x + i, y, array[y][x + i]])
                break
        for i in range(1, x + 1):
            if array[y][x - i] == " ":
                moves.append([x - i, y])
            else:
                if array[y][x - i] in "pnbrqk":
                    moves.append([x - i, y, array[y][x - i]])
                break
        for i in range(1, 8 - y):
            if array[y + i][x] == " ":
                moves.append([x, y + i])
            else:
                if array[y + i][x] in "pnbrqk":
                    moves.append([x, y + i, array[y + i][x]])
                break
        for i in range(1, y + 1):
            if array[y - i][x] == " ":
                moves.append([x, y - i])
            else:
                if array[y - i][x] in "pnbrqk":
                    moves.append([x, y - i, array[y - i][x]])
                break

    elif piece == "r" or piece == "q":
        for i in range(1, 8 - x):
            if array[y][x + i] == " ":
                moves.append([x + i, y])
            else:
                if array[y][x + i] in "PNBRQK":
                    moves.append([x + i, y, array[y][x + i]])
                break
        for i in range(1, x + 1):
            if array[y][x - i] == " ":
                moves.append([x - i, y])
            else:
                if array[y][x - i] in "PNBRQK":
                    moves.append([x - i, y, array[y][x - i]])
                break
        for i in range(1, 8 - y):
            if array[y + i][x] == " ":
                moves.append([x, y + i])
            else:
                if array[y + i][x] in "PNBRQK":
                    moves.append([x, y + i, array[y + i][x]])
                break
        for i in range(1, y + 1):
            if array[y - i][x] == " ":
                moves.append([x, y - i])
            else:
                if array[y - i][x] in "PNBRQK":
                    moves.append([x, y - i, array[y - i][x]])
                break

    if piece == "B" or piece == "Q":
        if x > y:
            for i in range(1, 8 - x):
                if array[y + i][x + i] == " ":
                    moves.append([x + i, y + i])
                else:
                    if array[y + i][x + i] in "pnbrqk":
                        moves.append([x + i, y + i, array[y + i][x + i]])
                    break
            for i in range(1, y + 1):
                if array[y - i][x - i] == " ":
                    moves.append([x - i, y - i])
                else:
                    if array[y - i][x - i] in "pnbrqk":
                        moves.append([x - i, y - i, array[y - i][x - i]])
                    break
        else:
            for i in range(1, 8 - y):
                if array[y + i][x + i] == " ":
                    moves.append([x + i, y + i])
                else:
                    if array[y + i][x + i] in "pnbrqk":
                        moves.append([x + i, y + i])
                    break
            for i in range(1, x + 1):
                if array[y - i][x - i] == " ":
                    moves.append([x - i, y - i])
                else:
                    if array[y - i][x - i] in "pnbrqk":
                        moves.append([x - i, y - i, array[y - i][x - i]])
                    break
        if 7 - x > y:
            for i in range(1, x + 1):
                if array[y + i][x - i] == " ":
                    moves.append([x - i, y + i])
                else:
                    if array[y + i][x - i] in "pnbrqk":
                        moves.append([x - i, y + i, array[y + i][x - i]])
                    break
            for i in range(1, y + 1):
                if array[y - i][x + i] == " ":
                    moves.append([x + i, y - i])
                else:
                    if array[y - i][x + i] in "pnbrqk":
                        moves.append([x + i, y - i, array[y - i][x + i]])
                    break
        else:
            for i in range(1, 8 - y):
                if array[y + i][x - i] == " ":
                    moves.append([x - i, y + i])
                else:
                    if array[y + i][x - i] in "pnbrqk":
                        moves.append([x - i, y + i, array[y + i][x - i]])
                    break
            for i in range(1, 8 - x):
                if array[y - i][x + i] == " ":
                    moves.append([x + i, y - i])
                else:
                    if array[y - i][x + i] in "pnbrqk":
                        moves.append([x + i, y - i, array[y - i][x + i]])
                    break

    elif piece == "b" or piece == "q":
        if x > y:
            for i in range(1, 8 - x):
                if array[y + i][x + i] == " ":
                    moves.append([x + i, y + i])
                else:
                    if array[y + i][x + i] in "PNBRQK":
                        moves.append([x + i, y + i, array[y + i][x + i]])
                    break
            for i in range(1, y + 1):
                if array[y - i][x - i] == " ":
                    moves.append([x - i, y - i])
                else:
                    if array[y - i][x - i] in "PNBRQK":
                        moves.append([x - i, y - i, array[y - i][x - i]])
                    break
        else:
            for i in range(1, 8 - y):
                if array[y + i][x + i] == " ":
                    moves.append([x + i, y + i])
                else:
                    if array[y + i][x + i] in "PNBRQK":
                        moves.append([x + i, y + i, array[y + i][x + i]])
                    break
            for i in range(1, x + 1):
                if array[y - i][x - i] == " ":
                    moves.append([x - i, y - i])
                else:
                    if array[y - i][x - i] in "PNBRQK":
                        moves.append([x - i, y - i, array[y - i][x - i]])
                    break
        if 7 - x > y:
            for i in range(1, x + 1):
                if array[y + i][x - i] == " ":
                    moves.append([x - i, y + i])
                else:
                    if array[y + i][x - i] in "PNBRQK":
                        moves.append([x - i, y + i, array[y + i][x - i]])
                    break
            for i in range(1, y + 1):
                if array[y - i][x + i] == " ":
                    moves.append([x + i, y - i])
                else:
                    if array[y - i][x + i] in "PNBRQK":
                        moves.append([x + i, y - i, array[y - i][x + i]])
                    break
        else:
            for i in range(1, 8 - y):
                if array[y + i][x - i] == " ":
                    moves.append([x - i, y + i])
                else:
                    if array[y + i][x - i] in "PNBRQK":
                        moves.append([x - i, y + i, array[y + i][x - i]])
                    break
            for i in range(1, 8 - x):
                if array[y - i][x + i] == " ":
                    moves.append([x + i, y - i])
                else:
                    if array[y - i][x + i] in "PNBRQK":
                        moves.append([x + i, y - i, array[y - i][x + i]])
                    break
    for i in moves:
        i.append(piece)
    return moves


def pawn_captures(piece, enpassant, array):
    mover = []
    moving = []
    if piece.colour == "White":
        potential_moves = [[piece.x - 2, piece.y, "P"], [piece.x, piece.y, "P"]]
        for j in potential_moves:
            if not (j[0] > 7 or j[1] > 7 or j[0] < 0 or j[1] < 0):
                moving.append(j)
        for j in moving:
            if array[j[1]][j[0]] in "pnbrqk":
                mover.append(j)
        if piece.y == 5:
            potential_moves = [[piece.x - 2, piece.y, "P"], [piece.x, piece.y, "P"]]
            for j in potential_moves:
                if not (j[0] > 7 or j[1] > 7 or j[0] < 0 or j[1] < 0):
                    moving.append(j)
            if enpassant[piece.x + 8] == "T" and array[moving[0][1] - 1][moving[0][0]] == "p":
                mover.append(moving[0])
            if enpassant[piece.x + 10] == "T" and array[moving[1][1] - 1][moving[1][0]] == "p":
                mover.append(moving[1])

    else:
        potential_moves = [[piece.x - 2, piece.y - 2, "p"], [piece.x, piece.y - 2, "p"]]
        for j in potential_moves:
            if not (j[0] > 7 or j[1] > 7 or j[0] < 0 or j[1] < 0):
                moving.append(j)
        for j in moving:
            if array[j[1]][j[0]] in "PNBRQK":
                mover.append(j)
        if piece.y == 4:
            potential_moves = [[piece.x - 2, piece.y - 2, "p"], [piece.x, piece.y - 2, "p"]]
            for j in potential_moves:
                if not (j[0] > 7 or j[1] > 7 or j[0] < 0 or j[1] < 0):
                    moving.append(j)
            if enpassant[piece.x - 1] == "T" and array[moving[0][1] + 1][moving[0][0]] == "P":
                mover.append(moving[0])
            if enpassant[piece.x + 1] == "T" and array[moving[1][1] + 1][moving[1][0]] == "P":
                mover.append(moving[1])
    return mover


def castles(piece, castle):
    print(castle)
    moves = []
    if piece.colour == "White":
        print(castle[4:8])
        print(castle[0:5])
        if castle[4:8] == "TTTT":
            moves.append([6, 0, "K"])
        if castle[0:5] == "TTTTT":
            moves.append([2, 0, "K"])

    else:
        if castle[12:] == "TTTT":
            moves.append([6, 7, "k"])
        if castle[8:13] == "TTTTT":
            moves.append([2, 7, "k"])
    return moves


def wouldcheck(array, new_piece, piece_num):
    opt = []
    remove = []
    x = 0
    y = 0
    move_list = new_piece.legal

    for i in range(len(move_list)):
        if move_list[i] != "0-0" and move_list[i] != "0-0-0":
            opt.append(move_list[i] + [piece_num])

    for a in range(len(opt)):
        arr = []
        for i in range(len(array)):
            arr.append(list(array[i]))
        chosen = opt[a]
        old_coord = [new_piece.x - 1, new_piece.y - 1]

        arr[old_coord[1]][old_coord[0]] = " "
        arr[chosen[1]][chosen[0]] = chosen[-2]

        if new_piece.colour == "White":
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[j][i] == "K":
                        x = i
                        y = j

            piece = []
            potential_moves = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1], [x - 2, y - 1],
                               [x - 1, y - 2],
                               [x + 1, y - 2], [x + 2, y - 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "n":
                    piece.append(moving[i])
                    piece.append(arr[moving[i][1]][moving[i][0]])

            potential_moves = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1],
                               [x, y - 1], [x + 1, y - 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "k":
                    piece.append(moving[i])
                    piece.append(arr[moving[i][1]][moving[i][0]])

            potential_moves = [[x - 1, y + 1], [x + 1, y + 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "p":
                    piece.append(moving[i])
                    piece.append(arr[moving[i][1]][moving[i][0]])
            if x > y:
                for i in range(1, 8 - x):
                    if arr[y + i][x + i] != " ":
                        if arr[y + i][x + i] in "bq":
                            piece.append([x + i, y + i])
                            piece.append(arr[y + i][x + i])
                        break
                for i in range(1, y + 1):
                    if arr[y - i][x - i] != " ":
                        if arr[y - i][x - i] in "bq":
                            piece.append([x - i, y - i])
                            piece.append(arr[y - i][x - i])
                        break
            else:
                for i in range(1, 8 - y):
                    if arr[y + i][x + i] != " ":
                        if arr[y + i][x + i] in "bq":
                            piece.append([x + i, y + i])
                            piece.append(arr[y + i][x + i])
                        break
                for i in range(1, x + 1):
                    if arr[y - i][x - i] != " ":
                        if arr[y - i][x - i] in "bq":
                            piece.append([x - i, y - i])
                            piece.append(arr[y - i][x - i])
                        break
            if 7 - x > y:
                for i in range(1, x + 1):
                    if arr[y + i][x - i] != " ":
                        if arr[y + i][x - i] in "bq":
                            piece.append([x - i, y + i])
                            piece.append(arr[y + i][x - i])
                        break
                for i in range(1, y + 1):
                    if arr[y - i][x + i] != " ":
                        if arr[y - i][x + i] in "bq":
                            piece.append([x + i, y - i])
                            piece.append(arr[y - i][x + i])
                        break
            else:
                for i in range(1, 8 - y):
                    if arr[y + i][x - i] != " ":
                        if arr[y + i][x - i] in "bq":
                            piece.append([x - i, y + i])
                            piece.append(arr[y + i][x - i])
                        break
                for i in range(1, 8 - x):
                    if arr[y - i][x + i] != " ":
                        if arr[y - i][x + i] in "bq":
                            piece.append([x + i, y - i])
                            piece.append(arr[y - i][x + i])
                        break
            for i in range(1, 8 - x):
                if arr[y][x + i] != " ":
                    if arr[y][x + i] in "rq":
                        piece.append([x + i, y])
                        piece.append(arr[y][x + i])
                    break
            for i in range(1, x + 1):
                if arr[y][x - i] != " ":
                    if arr[y][x - i] in "rq":
                        piece.append([x - i, y])
                        piece.append(arr[y][x - i])
                    break
            for i in range(1, 8 - y):
                if arr[y + i][x] != " ":
                    if arr[y + i][x] in "rq":
                        piece.append([x, y + i])
                        piece.append(arr[y + i][x])
                    break
            for i in range(1, y + 1):
                if arr[y - i][x] != " ":
                    if arr[y - i][x] in "rq":
                        piece.append([x, y - i])
                        piece.append(arr[y - i][x])
                    break
        else:
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[j][i] == "k":
                        x = i
                        y = j
            piece = []
            potential_moves = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1], [x - 2, y - 1],
                               [x - 1, y - 2],
                               [x + 1, y - 2], [x + 2, y - 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "N":
                    piece.append(moving[i])

            potential_moves = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1],
                               [x, y - 1], [x + 1, y - 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "K":
                    piece.append(moving[i])
                    piece.append(arr[moving[i][1]][moving[i][0]])

            potential_moves = [[x - 1, y - 1], [x + 1, y - 1]]
            moving = []
            for i in potential_moves:
                if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                    moving.append(i)
            for i in range(len(moving)):
                if arr[moving[i][1]][moving[i][0]] == "P":
                    piece.append(moving[i])
            if x > y:
                for i in range(1, 8 - x):
                    if arr[y + i][x + i] != " ":
                        if arr[y + i][x + i] in "BQ":
                            piece.append([x + i, y + i])
                            piece.append(arr[y + i][x + i])
                        break
                for i in range(1, y + 1):
                    if arr[y - i][x - i] != " ":
                        if arr[y - i][x - i] in "BQ":
                            piece.append([x - i, y - i])
                            piece.append(arr[y - i][x - i])
                        break
            else:
                for i in range(1, 8 - y):
                    if arr[y + i][x + i] != " ":
                        if arr[y + i][x + i] in "BQ":
                            piece.append([x + i, y + i])
                            piece.append(arr[y + i][x + i])
                        break
                for i in range(1, x + 1):
                    if arr[y - i][x - i] != " ":
                        if arr[y - i][x - i] in "BQ":
                            piece.append([x - i, y - i])
                            piece.append(arr[y - i][x - i])
                        break
            if 7 - x > y:
                for i in range(1, x - 1):
                    if arr[y + i][x - i] != " ":
                        if arr[y + i][x - i] in "BQ":
                            piece.append([x - i, y + i])
                            piece.append(arr[y + i][x - i])
                        break
                for i in range(1, y - 1):
                    if arr[y - i][x + i] != " ":
                        if arr[y - i][x + i] in "BQ":
                            piece.append([x + i, y - i])
                            piece.append(arr[y - i][x + i])
                        break
            else:
                for i in range(1, 8 - y):
                    if arr[y + i][x - i] != " ":
                        if arr[y + i][x - i] in "BQ":
                            piece.append([x - i, y + i])
                            piece.append(arr[y + i][x - i])
                        break
                for i in range(1, 8 - x):
                    if arr[y - i][x + i] != " ":
                        if arr[y - i][x + i] in "BQ":
                            piece.append([x + i, y - i])
                            piece.append(arr[y - i][x + i])
                        break
            for i in range(1, 8 - x):
                if arr[y][x + i] != " ":
                    if arr[y][x + i] in "RQ":
                        piece.append([x + i, y])
                        piece.append(arr[y][x + i])
                    break
            for i in range(1, x + 1):
                if arr[y][x - i] != " ":
                    if arr[y][x - i] in "RQ":
                        piece.append([x - i, y])
                        piece.append(arr[y][x - i])
                    break
            for i in range(1, 8 - y):
                if arr[y + i][x] != " ":
                    if arr[y + i][x] in "RQ":
                        piece.append([x, y + i])
                        piece.append(arr[y + i][x])
                    break
            for i in range(1, y + 1):
                if arr[y - i][x] != " ":
                    if arr[y - i][x] in "RQ":
                        piece.append([x, y - i])
                        piece.append(arr[y - i][x])
                    break

        if len(piece) >= 1:
            remove.append(opt[a][:-1])

    for i in range(len(move_list)):
        for j in range(len(move_list[i])):
            if move_list[i] in remove:
                move_list[i] = ""
            move_list[i] = [value for value in move_list[i] if value != ""]

    move_list = [value for value in move_list if value != []]

    if new_piece.abbr == "K" and new_piece.x == 5:
        if [5, 0, "K"] not in move_list and [6, 0, "K"] in move_list:
            move_list.remove([6, 0, "K"])
        if [3, 0, "K"] not in move_list and [2, 0, "K"] in move_list:
            move_list.remove([2, 0, "K"])
        if [5, 7, "k"] not in move_list and [6, 7, "k"] in move_list:
            move_list.remove([6, 7, "k"])
        if [3, 7, "k"] not in move_list and [2, 7, "k"] in move_list:
            move_list.remove([2, 7, "k"])

    return move_list


def check(arr, king):
    opt = []
    remove = []
    x = king.x - 1
    y = king.y - 1

    if king.colour == "White":

        piece = []
        potential_moves = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1], [x - 2, y - 1],
                           [x - 1, y - 2],
                           [x + 1, y - 2], [x + 2, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "n":
                piece.append(moving[i])
                piece.append(arr[moving[i][1]][moving[i][0]])

        potential_moves = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1],
                           [x, y - 1], [x + 1, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "k":
                piece.append(moving[i])
                piece.append(arr[moving[i][1]][moving[i][0]])

        potential_moves = [[x - 1, y + 1], [x + 1, y + 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "p":
                piece.append(moving[i])
                piece.append(arr[moving[i][1]][moving[i][0]])
        if x > y:
            for i in range(1, 8 - x):
                if arr[y + i][x + i] != " ":
                    if arr[y + i][x + i] in "bq":
                        piece.append([x + i, y + i])
                        piece.append(arr[y + i][x + i])
                    break
            for i in range(1, y + 1):
                if arr[y - i][x - i] != " ":
                    if arr[y - i][x - i] in "bq":
                        piece.append([x - i, y - i])
                        piece.append(arr[y - i][x - i])
                    break
        else:
            for i in range(1, 8 - y):
                if arr[y + i][x + i] != " ":
                    if arr[y + i][x + i] in "bq":
                        piece.append([x + i, y + i])
                        piece.append(arr[y + i][x + i])
                    break
            for i in range(1, x + 1):
                if arr[y - i][x - i] != " ":
                    if arr[y - i][x - i] in "bq":
                        piece.append([x - i, y - i])
                        piece.append(arr[y - i][x - i])
                    break
        if 7 - x > y:
            for i in range(1, x + 1):
                if arr[y + i][x - i] != " ":
                    if arr[y + i][x - i] in "bq":
                        piece.append([x - i, y + i])
                        piece.append(arr[y + i][x - i])
                    break
            for i in range(1, y + 1):
                if arr[y - i][x + i] != " ":
                    if arr[y - i][x + i] in "bq":
                        piece.append([x + i, y - i])
                        piece.append(arr[y - i][x + i])
                    break
        else:
            for i in range(1, 8 - y):
                if arr[y + i][x - i] != " ":
                    if arr[y + i][x - i] in "bq":
                        piece.append([x - i, y + i])
                        piece.append(arr[y + i][x - i])
                    break
            for i in range(1, 8 - x):
                if arr[y - i][x + i] != " ":
                    if arr[y - i][x + i] in "bq":
                        piece.append([x + i, y - i])
                        piece.append(arr[y - i][x + i])
                    break
        for i in range(1, 8 - x):
            if arr[y][x + i] != " ":
                if arr[y][x + i] in "rq":
                    piece.append([x + i, y])
                    piece.append(arr[y][x + i])
                break
        for i in range(1, x + 1):
            if arr[y][x - i] != " ":
                if arr[y][x - i] in "rq":
                    piece.append([x - i, y])
                    piece.append(arr[y][x - i])
                break
        for i in range(1, 8 - y):
            if arr[y + i][x] != " ":
                if arr[y + i][x] in "rq":
                    piece.append([x, y + i])
                    piece.append(arr[y + i][x])
                break
        for i in range(1, y + 1):
            if arr[y - i][x] != " ":
                if arr[y - i][x] in "rq":
                    piece.append([x, y - i])
                    piece.append(arr[y - i][x])
                break
    else:
        piece = []
        potential_moves = [[x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2], [x + 2, y + 1], [x - 2, y - 1],
                           [x - 1, y - 2],
                           [x + 1, y - 2], [x + 2, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "N":
                piece.append(moving[i])

        potential_moves = [[x + 1, y], [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1],
                           [x, y - 1], [x + 1, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "K":
                piece.append(moving[i])
                piece.append(arr[moving[i][1]][moving[i][0]])

        potential_moves = [[x - 1, y - 1], [x + 1, y - 1]]
        moving = []
        for i in potential_moves:
            if not (i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0):
                moving.append(i)
        for i in range(len(moving)):
            if arr[moving[i][1]][moving[i][0]] == "P":
                piece.append(moving[i])
        if x > y:
            for i in range(1, 8 - x):
                if arr[y + i][x + i] != " ":
                    if arr[y + i][x + i] in "BQ":
                        piece.append([x + i, y + i])
                        piece.append(arr[y + i][x + i])
                    break
            for i in range(1, y + 1):
                if arr[y - i][x - i] != " ":
                    if arr[y - i][x - i] in "BQ":
                        piece.append([x - i, y - i])
                        piece.append(arr[y - i][x - i])
                    break
        else:
            for i in range(1, 8 - y):
                if arr[y + i][x + i] != " ":
                    if arr[y + i][x + i] in "BQ":
                        piece.append([x + i, y + i])
                        piece.append(arr[y + i][x + i])
                    break
            for i in range(1, x + 1):
                if arr[y - i][x - i] != " ":
                    if arr[y - i][x - i] in "BQ":
                        piece.append([x - i, y - i])
                        piece.append(arr[y - i][x - i])
                    break
        if 7 - x > y:
            for i in range(1, x - 1):
                if arr[y + i][x - i] != " ":
                    if arr[y + i][x - i] in "BQ":
                        piece.append([x - i, y + i])
                        piece.append(arr[y + i][x - i])
                    break
            for i in range(1, y - 1):
                if arr[y - i][x + i] != " ":
                    if arr[y - i][x + i] in "BQ":
                        piece.append([x + i, y - i])
                        piece.append(arr[y - i][x + i])
                    break
        else:
            for i in range(1, 8 - y):
                if arr[y + i][x - i] != " ":
                    if arr[y + i][x - i] in "BQ":
                        piece.append([x - i, y + i])
                        piece.append(arr[y + i][x - i])
                    break
            for i in range(1, 8 - x):
                if arr[y - i][x + i] != " ":
                    if arr[y - i][x + i] in "BQ":
                        piece.append([x + i, y - i])
                        piece.append(arr[y - i][x + i])
                    break
        for i in range(1, 8 - x):
            if arr[y][x + i] != " ":
                if arr[y][x + i] in "RQ":
                    piece.append([x + i, y])
                    piece.append(arr[y][x + i])
                break
        for i in range(1, x + 1):
            if arr[y][x - i] != " ":
                if arr[y][x - i] in "RQ":
                    piece.append([x - i, y])
                    piece.append(arr[y][x - i])
                break
        for i in range(1, 8 - y):
            if arr[y + i][x] != " ":
                if arr[y + i][x] in "RQ":
                    piece.append([x, y + i])
                    piece.append(arr[y + i][x])
                break
        for i in range(1, y + 1):
            if arr[y - i][x] != " ":
                if arr[y - i][x] in "RQ":
                    piece.append([x, y - i])
                    piece.append(arr[y - i][x])
                break

    if len(piece) >= 1:
        return True
    else:
        return False


def choose_move(selected, a, b):
    legal = []
    for i in selected.legal:
        legal.append([i[0] + 1, i[1] + 1])
    for i in range(len(legal)):
        if [a, b] == legal[i]:
            return selected.legal[i]
    return None


def update(layout, end, castle, promotion, turn, arr, chosen, index):
    coord = str(chosen[0] + 1) + str(chosen[1] + 1)
    side = ""
    if turn % 2 == 1:
        position = layout
        piece = layout[index * 3:index * 3 + 3]
        if coord in layout:
            arr[int(coord[1]) - 1][int(coord[0]) - 1] = " "
            position = position[0:position.index(coord) - 1] + "x00" + position[position.index(coord) + 2:]
        elif piece[0] == "P" and int(piece[1]) - 1 != chosen[0]:
            enp_coord = str(chosen[0] + 1) + str(chosen[1])
            arr[int(enp_coord[1]) - 1][int(enp_coord[0]) - 1] = " "
            position = position[0:position.index(enp_coord) - 1] + "x00" + position[position.index(enp_coord) + 2:]
        arr[int(piece[2]) - 1][int(piece[1]) - 1] = " "
        arr[int(coord[1]) - 1][int(coord[0]) - 1] = piece[0]
        if chosen == [6, 0, "K"] and piece[1]=="5":
            arr[0][7] = " "
            arr[0][5] = "R"
            position = position[0:22] + "61" + position[24:]
            side = "O-O"
        elif chosen == [2, 0, "K"] and piece[1]=="5":
            arr[0][0] = " "
            arr[0][3] = "R"
            position = position[0:1] + "41" + position[3:]
            side = "O-O-O"
        ui = []
        for i in range(8):
            ui.append(arr[7 - i])
        for i in range(8):
            print(" ".join(ui[i]))

        position = position[0:index * 3 + 1] + coord + position[index * 3 + 3:]
        castling = castle
        if arr[0][1] == " ":
            castling = "T" + castling[1:]
        else:
            castling = "F" + castling[1:]
        if arr[0][2] == " ":
            castling = castling[0:1] + "T" + castling[2:]
        else:
            castling = castling[0:1] + "F" + castling[2:]
        if arr[0][2] == " ":
            castling = castling[0:2] + "T" + castling[3:]
        else:
            castling = castling[0:2] + "F" + castling[3:]
        if arr[0][5] == " ":
            castling = castling[0:6] + "T" + castling[7:]
        else:
            castling = castling[0:6] + "F" + castling[7:]
        if arr[0][6] == " ":
            castling = castling[0:7] + "T" + castling[8:]
        else:
            castling = castling[0:7] + "F" + castling[8:]
        if position[1:3] != "11":
            castling = castling[0:3] + "F" + castling[4:]
        if position[13:15] != "51":
            castling = castling[0:4] + "F" + castling[5:]
        if position[22:24] != "81":
            castling = castling[0:5] + "F" + castling[6:]

        passant = "XFFFFFFFFXFFFFFFFFX"
        if piece[0] == "P" and piece[2] == "2" and coord[1] == "4":
            passant = passant[0:int(piece[1])] + "T" + passant[int(piece[1]) + 1:]

    else:
        position = layout
        piece = layout[(index + 16) * 3:(index + 17) * 3]
        if coord in layout:
            arr[int(coord[1]) - 1][int(coord[0]) - 1] = " "
            position = position[0:position.index(coord) - 1] + "X00" + position[position.index(coord) + 2:]
        elif piece[0] == "p" and int(piece[1]) - 1 != chosen[0]:
            enp_coord = str(chosen[0] + 1) + str(chosen[1] + 2)
            arr[int(enp_coord[1]) - 1][int(enp_coord[0]) - 1] = " "
            position = position[0:position.index(enp_coord) - 1] + "X00" + position[position.index(enp_coord) + 2:]
        arr[int(piece[2]) - 1][int(piece[1]) - 1] = " "
        arr[int(coord[1]) - 1][int(coord[0]) - 1] = piece[0]
        if chosen == [6, 7, "k"] and piece[1]=="5":
            arr[7][7] = " "
            arr[7][5] = "r"
            position = position[0:70] + "68" + position[72:]
            side = "O-O"
        elif chosen == [2, 7, "k"] and piece[1]=="5":
            arr[7][0] = " "
            arr[7][3] = "r"
            position = position[0:49] + "48" + position[51:]
            side = "O-O-O"
        ui = []
        for i in range(8):
            ui.append(arr[7 - i])
        for i in range(8):
            print(" ".join(ui[i]))

        if coord in position:
            position = position[0:position.index(coord) - 1] + "X00" + position[position.index(coord) + 2:]

        position = position[0:(index + 16) * 3 + 1] + coord + position[(index + 16) * 3 + 3:]

        castling = castle
        if arr[7][1] == " ":
            castling = castling[0:8] + "T" + castling[9:]
        else:
            castling = castling[0:8] + "F" + castling[9:]
        if arr[7][2] == " ":
            castling = castling[0:9] + "T" + castling[10:]
        else:
            castling = castling[0:9] + "F" + castling[10:]
        if arr[7][3] == " ":
            castling = castling[0:10] + "T" + castling[11:]
        else:
            castling = castling[0:10] + "F" + castling[11:]
        if arr[7][5] == " ":
            castling = castling[0:14] + "T" + castling[15:]
        else:
            castling = castling[0:14] + "F" + castling[15:]
        if arr[7][6] == " ":
            castling = castling[0:15] + "T"
        else:
            castling = castling[0:15] + "F"
        if position[49:51] != "18":
            castling = castling[0:11] + "F" + castling[12:]
        if position[61:63] != "58":
            castling = castling[0:12] + "F" + castling[13:]
        if position[70:72] != "88":
            castling = castling[0:13] + "F" + castling[14:]

        passant = "XFFFFFFFFXFFFFFFFFX"
        if piece[0] == "p" and piece[2] == "7" and coord[1] == "5":
            passant = passant[0:int(piece[1]) + 9] + "T" + passant[int(piece[1]):+ 10]

    return position, end, passant, castling, promotion, arr, side


###################################################################################################################

def board_draw():
    game_display.fill(black)

    pygame.draw.rect(game_display, white, (10, 10, 670, 670))
    pygame.draw.rect(game_display, light, (690, 10, 580, 670))
    pygame.draw.rect(game_display, dark, (700, 20, 560, 60))
    pygame.draw.rect(game_display, dark, (700, 90, 560, 400))
    pygame.draw.rect(game_display, dark, (700, 500, 215, 170))
    pygame.draw.rect(game_display, dark, (925, 500, 335, 170))
    pygame.draw.rect(game_display, red, (1160, 30, 90, 40))
    for i in range(8):
        if i % 2 == 0:
            j = 0
        else:
            j = 1
        while j < 8:
            pygame.draw.rect(game_display, light, (i * 80 + 40, j * 80 + 10, block_width, block_height))
            j += 2
    for i in range(8):
        if i % 2 == 1:
            j = 0
        else:
            j = 1
        while j < 8:
            pygame.draw.rect(game_display, dark, (i * 80 + 40, j * 80 + 10, block_width, block_height))
            j += 2


def select_block(x_cursor, y_cursor, pieces):
    selected_piece = None
    for i in range(len(pieces)):
        if pieces[i].x == x_cursor and pieces[i].y == y_cursor:
            return pieces[i]


def main():
    layout = "R11N21B31Q41K51B61N71R81P12P22P32P42P52P62P72P82r18n28b38q48k58b68n78r88p17p27p37p47p57p67p77p87"
    end = "FFFFF"
    enpassant = "XFFFFFFFFXFFFFFFFFX"
    castle = "FFFTTTFFFFFTTTFF"
    promotion = "FFFFFFFFF"
    turn = 1
    turn_list = []
    selected_piece = None
    selected_family = "White"
    select = False
    flag = True
    over = False
    reset = False
    number_taken = 0
    white_pieces = [Piece(1, 1, "White", "R"), Piece(2, 1, "White", "N"), Piece(3, 1, "White", "B"),
                    Piece(4, 1, "White", "Q"),
                    Piece(5, 1, "White", "K"), Piece(6, 1, "White", "B"), Piece(7, 1, "White", "N"),
                    Piece(8, 1, "White", "R"),
                    Piece(1, 2, "White", "P"), Piece(2, 2, "White", "P"), Piece(3, 2, "White", "P"),
                    Piece(4, 2, "White", "P"),
                    Piece(5, 2, "White", "P"), Piece(6, 2, "White", "P"), Piece(7, 2, "White", "P"),
                    Piece(8, 2, "White", "P")]
    black_pieces = [Piece(1, 8, "Black", "R"), Piece(2, 8, "Black", "N"), Piece(3, 8, "Black", "B"),
                    Piece(4, 8, "Black", "Q"),
                    Piece(5, 8, "Black", "K"), Piece(6, 8, "Black", "B"), Piece(7, 8, "Black", "N"),
                    Piece(8, 8, "Black", "R"),
                    Piece(1, 7, "Black", "P"), Piece(2, 7, "Black", "P"), Piece(3, 7, "Black", "P"),
                    Piece(4, 7, "Black", "P"),
                    Piece(5, 7, "Black", "P"), Piece(6, 7, "Black", "P"), Piece(7, 7, "Black", "P"),
                    Piece(8, 7, "Black", "P")]
    empty_piece = Piece(0, 0, None, None)
    pieces = white_pieces + black_pieces
    array = setup(white_pieces, black_pieces)

    turn_font = pygame.font.Font("overpass.otf", 30)
    my_font = pygame.font.Font("overpass.otf", 25)
    move_font = pygame.font.Font("overpass.otf", 12)
    reset_font = pygame.font.Font("overpass.otf", 18)
    reset_button = reset_font.render("Reset", True, white)
    reset_button1 = reset_font.render("board", True, white)
    result_string = my_font.render("... wins", True, white)

    while True:
        if flag:
            own_squares = []
            if selected_family == "White":
                own_pieces = white_pieces
            else:
                own_pieces = black_pieces
            for i in own_pieces:
                own_squares.append(str(i.x) + str(i.y))
            own_pieces[4].in_check = check(array, own_pieces[4])
            if own_pieces[4].in_check:
                turn_list[-1] = turn_list[-1] + "+"

            move = []
            for i in own_pieces:
                if not i.taken:
                    if selected_family == "White":
                        i.legal = valid(i.abbr, i.x - 1, i.y - 1, array)
                    else:
                        i.legal = valid(i.abbr.lower(), i.x - 1, i.y - 1, array)
                    if i.abbr == "P":
                        pawn = pawn_captures(i, enpassant, array)
                        for j in pawn:
                            i.legal.append(j)
                    elif i.abbr == "K" and not i.in_check:
                        castling = castles(i, castle)
                        for j in castling:
                            i.legal.append(j)
                    if i.legal != []:
                        i.legal = wouldcheck(array, i, own_pieces.index(i))
                    move.append(i.legal)
            print(own_pieces[4].in_check)
            print(move)
            over = True
            for i in move:
                if i != []:
                    over = False
            if over:
                print("Over")
                if turn_list[-1][-1] == "+":
                    turn_list[-1] = turn_list[-1][:-1] + "#"
            flag = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                a = (pos[0] + 40) // 80
                b = 8 - ((pos[1] - 10) // 80)
                coord = str(a) + str(b)
                if 9 > a > 0 and 9 > b > 0:

                    if coord in own_squares or not select:
                        selected_piece = select_block(a, b, pieces)
                        if selected_piece is not None:
                            if selected_piece.legal != []:
                                select = True

                    else:
                        if selected_piece is not None:
                            if selected_piece.colour == selected_family:
                                original_coord = [selected_piece.x, selected_piece.y]
                                isvalid = choose_move(selected_piece, a, b)
                                piece_index = own_pieces.index(selected_piece)
                                if isvalid is not None:

                                    layout, end, enpassant, castle, promotion, array, side = update(layout, end, castle,
                                                                                                    promotion, turn,
                                                                                                    array, isvalid,
                                                                                                    piece_index)
                                    for i in range(len(pieces)):
                                        pieces[i].x = int(layout[3 * i + 1])
                                        pieces[i].y = int(layout[3 * i + 2])
                                        if layout[3 * i].lower() == "x":
                                            pieces[i].taken = True
                                    files = "abcdefgh"

                                    new_number_taken = 0
                                    for i in pieces:
                                        if i.taken:
                                            new_number_taken += 1
                                    if turn % 2 == 1:
                                        if side != "":
                                            turn_list.append(
                                                str(turn // 2 + 1) + "." + side)
                                        elif isvalid[-1] == "P":
                                            if new_number_taken > number_taken:
                                                turn_list.append(
                                                    str(turn // 2 + 1) + "." + files[original_coord[0] - 1] + "x" +
                                                    files[isvalid[0]] + str(isvalid[1] + 1))
                                            else:
                                                turn_list.append(
                                                    str(turn // 2 + 1) + "." + files[isvalid[0]] + str(isvalid[1] + 1))
                                        else:
                                            if new_number_taken > number_taken:
                                                turn_list.append(str(turn // 2 + 1) + "." + isvalid[-1] + "x" + files[
                                                    isvalid[0]] + str(isvalid[1] + 1))
                                            else:
                                                turn_list.append(
                                                    str(turn // 2 + 1) + "." + isvalid[-1] + files[isvalid[0]] + str(
                                                        isvalid[1] + 1))
                                        selected_family = "Black"
                                    else:
                                        if side != "":
                                            turn_list.append(side)
                                        elif isvalid[-1] == "p":
                                            if new_number_taken > number_taken:
                                                turn_list.append(
                                                    files[original_coord[0] - 1] + "x" + files[isvalid[0]] + str(
                                                        isvalid[1] + 1))
                                            else:
                                                turn_list.append(files[isvalid[0]] + str(isvalid[1] + 1))
                                        else:
                                            if new_number_taken > number_taken:
                                                turn_list.append(
                                                    isvalid[-1].upper() + "x" + files[isvalid[0]] + str(isvalid[1] + 1))
                                            else:
                                                turn_list.append(
                                                    isvalid[-1].upper() + files[isvalid[0]] + str(isvalid[1] + 1))
                                        selected_family = "White"
                                    for i in own_pieces:
                                        i.legal = []
                                    turn += 1
                                    flag = True
                                    number_taken = new_number_taken

                        selected_piece = None
                        select = False
                if 1160 < pos[0] < 1250 and 30 < pos[1] < 70:
                    if reset:
                        reset = False
                        main()
                    else:
                        reset = True
                        reset_button = reset_font.render("Click to", True, white)
                        reset_button1 = reset_font.render("confirm", True, white)
                else:
                    reset = False
                    reset_button = reset_font.render("Reset", True, white)
                    reset_button1 = reset_font.render("board", True, white)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if turn >= 200:
            over = True

        if over:
            if black_pieces[4].in_check:
                end = "TFFFF"
                result_string = my_font.render("White wins", True, white)
                turn_list.append("1-0")
            elif white_pieces[4].in_check:
                end = "FTFFF"
                result_string = my_font.render("Black wins", True, white)
                turn_list.append("0-1")
            else:
                end = "FFTFF"
                result_string = my_font.render("Draw", True, white)
                turn_list.append("1/2-1/2")
            over = False
            flag = False

        string = selected_family + "'s turn"
        label = turn_font.render(string, True, white)
        label_board = []
        for i in "abcdefgh":
            label_board.append(my_font.render(i, True, black))
        for i in range(8):
            label_board.append(my_font.render(str(i + 1), True, black))
        length=0
        temp_list = turn_list
        notate = ""
        i=0
        text = []
        while len(temp_list)>0:
            while length<=75:
                print(i)
                print(len(temp_list))
                if i + 1 == len(temp_list):
                    break
                notate += temp_list[i]
                i+=1
                length += len(temp_list[i])
                print(notate)
            temp_list.remove(notate)
            text.append(" ".join(notate))
        label_turn = []
        for i in text:
            label_turn.append(move_font.render(i, True, white))
        move_string = my_font.render("Moves", True, white)
        clock_string = my_font.render("Clock", True, white)
        white_string = move_font.render("White:", True, white)
        black_string = move_font.render("Black:", True, white)
        white_clock = turn_font.render("00:00", True, white)
        black_clock = turn_font.render("00:00", True, white)
        out_date = time.strftime('%Y/%m/%d', time.localtime())
        out_time = time.strftime('%H:%M:%S', time.localtime())
        date_string = reset_font.render(out_date, True, white)
        time_string = turn_font.render(out_time, True, white)

        board_draw()
        initialize_piece(pieces)
        initialize_taken(move_font, my_font, pieces)
        if selected_piece != None:
            initialise_circle(selected_piece)
            if selected_piece.legal != []:
                pygame.draw.rect(game_display, teal, (
                    (selected_piece.x - 1) * 80 + 42, (8 - selected_piece.y) * 80 + 12, block_width - 4,
                    block_height - 4),
                                 5)
        else:
            initialise_circle(empty_piece)

        game_display.blit(label, (10, 680))
        for i in range(8):
            game_display.blit(label_board[i], (80 * i + 70, 645))
        for i in range(8):
            game_display.blit(label_board[15 - i], (15, 80 * i + 35))
        for i in range(len(label_turn)):
            game_display.blit(label_turn[i], (710, 16 * i + 125))
        move_rect = move_string.get_rect(center=(980, 110))
        game_display.blit(move_string, move_rect)
        game_display.blit(clock_string, (935, 635))
        game_display.blit(white_string, (935, 510))
        game_display.blit(black_string, (935, 570))
        game_display.blit(white_clock, (935, 525))
        game_display.blit(black_clock, (935, 585))
        game_display.blit(result_string, (710, 45))
        reset_rect = reset_button.get_rect(center=(1205, 40))
        reset1_rect = reset_button1.get_rect(center=(1205, 60))
        game_display.blit(reset_button, reset_rect)
        game_display.blit(reset_button1, reset1_rect)
        date_rect = date_string.get_rect(center=(980, 65))
        time_rect = time_string.get_rect(center=(980, 40))
        game_display.blit(date_string, date_rect)
        game_display.blit(time_string, time_rect)
        pygame.display.update()

        clock.tick(60)  # max fps


if __name__ == "__main__":
    main()

