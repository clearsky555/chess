from figures.bishop import Bishop
from figures.figure import all_figures
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
import matplotlib.pyplot as plt
from figures.queen import Queen
from figures.rook import Rook


print('Это шахматный эмулятор. Выберите название фигуры, координаты хода и закройте окно для ввода')

# БЕЛЫЕ ФИГУРЫ
p1 = Pawn(1,2,1, 'пешка1')
# p1.name = 'пешка1'
# print(p1.__dict__)

p2 = Pawn(2,2,1, 'пешка2')
# p2.name = 'пешка2'

p3 = Pawn(3,2,1,'пешка3')
# p3.name = 'пешка3'

p4 = Pawn(4,2,1, 'пешка4')
# p4.name = 'пешка4'

p5 = Pawn(5,2,1, 'пешка5')
# p5.name = 'пешка5'

p6 = Pawn(6,2,1, 'пешка6')
# p6.name = 'пешка6'

p7 = Pawn(7,2,1, 'пешка7')
# p7.name = 'пешка7'

p8 = Pawn(8,2,1, 'пешка8')
# p8.name = 'пешка8'

r1 = Rook(1,1,1,'ладья1')
# r1.name = 'ладья1'

r2 = Rook(8,1,1, 'ладья2')
# r2.name = 'ладья2'

k1 = Knight(2,1,1, 'конь1')
# k1.name = 'конь1'

k2 = Knight(7,1,1, 'конь2')
# k2.name = 'конь2'

b1 = Bishop(3,1,1, 'слон1')
# b1.name = 'слон1'

b2 = Bishop(6,1,1, 'слон2')
# b2.name = 'слон2'

q = Queen(4,1,1, 'ферзь')
# q.name = 'ферзь'

k = King(5,1,1, 'король')
# k.name = 'король'

#ЧЕРНЫЕ ФИГУРЫ
p9 = Pawn(1,7,2,'пешка1b')
# p9.name = 'пешка1'

p10 = Pawn(2,7,2,'пешка2b')
# p10.name = 'пешка2'

p11 = Pawn(3,7,2,'пешка3b')
# p11.name = 'пешка3'

p12 = Pawn(4,7,2,'пешка4b')
# p12.name = 'пешка4'

p13 = Pawn(5,7,2,'пешка5b')
# p13.name = 'пешка5'

p14 = Pawn(6,7,2,'пешка6b')
# p14.name = 'пешка6'

p15 = Pawn(7,7,2,'пешка7b')
# p15.name = 'пешка7'

p16 = Pawn(8,7,2,'пешка8b')
# p16.name = 'пешка8'

r3 = Rook(1,8,2,'ладья1b')
# r3.name = 'ладья1'

r4 = Rook(8,8,2,'ладья2b')
# r4.name = 'ладья2'

k3 = Knight(2,8,2,'конь1b')
# k3.name = 'конь1'

k4 = Knight(7,8,2,'конь2b')
# k4.name = 'конь2'

b3 = Bishop(3,8,2,'слон1b')
# b3.name = 'слон1'

b4 = Bishop(6,8,2,'слон2b')
# b4.name = 'слон2'

qq = Queen(4,8,2,'ферзьb')
# qq.name = 'ферзь'

kk = King(5,8,2,'корольb')
# kk.name = 'король'



board = [
     [ 25, 150, 25, 150, 25, 150, 25, 150],
     [ 150, 25, 150, 25, 150, 25, 150, 25],
     [25, 150, 25, 150, 25, 150, 25, 150],
     [150, 25, 150, 25, 150, 25, 150, 25],
     [25, 150, 25, 150, 25, 150, 25, 150],
     [150, 25, 150, 25, 150, 25, 150, 25],
     [25, 150, 25, 150, 25, 150, 25, 150],
     [150, 25, 150, 25, 150, 25, 150, 25],
     ]

fig, ax = plt.subplots()
ax.pcolor(board, cmap='Accent')


# ходы для проверки
# print(len(all_coords))
# print(len(all_figures))

# отображения фигур на доске в виде текста
for x in all_figures:
     ax.text(x.x - 1, x.y - 1, x.name)


plt.show()

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
        elif figure_name[0] == figure.name:
            a, b = int(figure_name[1]), int(figure_name[2])
            figure.move(a, b)
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



    fig, ax = plt.subplots()
    ax.pcolor(board, cmap='Accent')
    for x in all_figures:
         ax.text(x.x - 1, x.y - 1, x.name)
    plt.show()
