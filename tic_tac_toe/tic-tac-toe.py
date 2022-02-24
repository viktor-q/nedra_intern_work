import random
from time import sleep

import numpy as np


# Создание поля
def create_board(vertical, horizontal):
    board = np.zeros((vertical, horizontal), dtype=int)
    return board


# Проверка пустых мест
def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return l


# Выбор рандомного места
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board


# Проверка трех одинаковых знаков в горизонтальном ряду
def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return win
        return win


# Проверка трех одинаковых знаков по вертикали
def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return win
        return win


# Проверка трех одинаковых знаков по диагонали
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win


# Выбор результата игры
def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


# Функция для запуска игры
def play_game(vertical, horizontal):
    board, winner, counter = create_board(vertical, horizontal), 0, 1
    print(board)
    sleep(1)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Поле после " + str(counter) + " попытки")
            print(board)
            sleep(1)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


# Вывод результата игры

result = play_game(3, 3)
if result == 1:
    print("Победил игрок 1")
if result == 2:
    print("Победил игрок 2")
if result == -1:
    print("Ничья")
