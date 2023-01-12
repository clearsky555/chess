from matplotlib import pyplot as plt
from figures.bishop import Bishop
from figures.figure import all_figures
from figures.king import King
from figures.knight import Knight
from figures.queen import Queen
from figures.rook import Rook
move_counter = 0

def make_board():
    W = 25
    B = 150
    board = [
        [W, B, W, B, W, B, W, B],
        [B, W, B, W, B, W, B, W],
        [W, B, W, B, W, B, W, B],
        [B, W, B, W, B, W, B, W],
        [W, B, W, B, W, B, W, B],
        [B, W, B, W, B, W, B, W],
        [W, B, W, B, W, B, W, B],
        [B, W, B, W, B, W, B, W],
    ]

    fig, ax = plt.subplots()
    ax.pcolor(board, cmap='Accent')
    for x in all_figures:
        ax.text(x.x - 1, x.y - 1, x.name)
    plt.show()

def show_menu(move_counter=0):
    while True:
        figure_name = input('введите название фигуры и координаты хода: ').split()
        for figure in all_figures:
            if figure_name[0] == figure.name and isinstance(figure, King):
                print('1.рокировка')
                print('2.ход')
                command = int(input('выберите команду: '))
                if command == 1:
                    rook_name = input('выберите ладью: ')
                    for figure1 in all_figures:
                        if rook_name == figure1.name and isinstance(figure1, Rook):
                            figure.castling(figure1)
                elif command == 2:
                    a, b = int(figure_name[1]), int(figure_name[2])
                    figure.move(a, b)

                    # ЗДЕСЬ НАДО ДОДЕЛАТЬ ОЧЕРЕДНОСТЬ ХОДОВ

                    move_counter += 1
                    print(move_counter)
            elif figure_name[0] == figure.name:
                a, b = int(figure_name[1]), int(figure_name[2])
                figure.move(a, b)

                # ЗДЕСЬ НАДО ДОДЕЛАТЬ ОЧЕРЕДНОСТЬ ХОДОВ

                move_counter += 1
                print(move_counter)
                if figure.color == 1 and move_counter % 2 == 0:
                    print('сейчас очередь черных')

                # ЗДЕСЬ НАДО ДОДЕЛАТЬ ОЧЕРЕДНОСТЬ ХОДОВ

                if 'пешка' in figure.name and figure.color == 1 and figure.y == 8:
                    command1 = int(input('выберите вместо пешки любую фигуру: 1. ладья 2. конь 3. слон 4 ферзь'))
                    if command1 == 1:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure1 = Rook(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 2:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure2 = Knight(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 3:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure3 = Bishop(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 4:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure4 = Queen(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)

                elif 'пешка' in figure.name and figure.color == 2 and figure.y == 1:
                    command1 = int(input('выберите вместо пешки любую фигуру: 1. ладья 2. конь 3. слон 4 ферзь'))
                    if command1 == 1:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure5 = Rook(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 2:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure6 = Knight(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 3:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure7 = Bishop(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)
                    elif command1 == 4:
                        new_figure = input('выберите название фигуры: ')
                        for x in all_figures:
                            while x.name == new_figure:
                                print('это название уже занято')
                                new_figure = input('выберите название фигуры: ')
                        New_figure8 = Queen(figure.x, figure.y, figure.color, new_figure)
                        all_figures.remove(figure)

        make_board()