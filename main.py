from figures.bishop import Bishop
from figures.figure import all_coords, all_figures
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
import matplotlib.pyplot as plt

from figures.queen import Queen
from figures.rook import Rook

print('Это шахматный эмулятор. Выберите фигуру')

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
# print(p9.__dict__)

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

board = [[ 0, 1, 0, 1, 0, 1, 0, 1],
     [ 1, 0, 1, 0, 1, 0, 1, 0],
     [ 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0],
     [ 0, 1, 0, 1, 0, 1, 0, 1],
     [ 1, 0, 1, 0, 1, 0, 1, 0],
     [ 0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0]
     ]

fig, ax = plt.subplots()
ax.pcolormesh(board)

# ходы для проверки
# print(len(all_coords))
# print(len(all_figures))
# k3.move(3,6)
# b3.move(5,6)
# qq.move(4,6)
# kk.castling(r3)
# p9.move(1,5)
# p9.move(1,3)


# print(len(all_coords))
# print(len(all_figures))


# r1.move(1,8)

# отображения фигур на доске в виде текста
for x in all_figures:
     ax.text(x.x - 1, x.y - 1, x.name)

# ax.text(k.x-1, k.y-1, k.name, color = 'white')
# ax.text(p1.x-1, p1.y-1, p1.name, color = 'white')
# ax.text(p2.x-1, p2.y-1, p2.name, color = 'white')
# ax.text(p3.x-1, p3.y-1, p3.name, color = 'white')
# ax.text(p4.x-1, p4.y-1, p4.name, color = 'white')
# ax.text(p5.x-1, p5.y-1, p5.name, color = 'white')
# ax.text(p6.x-1, p6.y-1, p6.name, color = 'white')
# ax.text(p7.x-1, p7.y-1, p7.name, color = 'white')
# ax.text(p8.x-1, p8.y-1, p8.name, color = 'white')
# ax.text(r1.x-1, r1.y-1, r1.name, color = 'white')
# ax.text(r2.x-1, r2.y-1, r2.name, color = 'white')
# ax.text(k1.x-1, k1.y-1, k1.name, color = 'white')
# ax.text(k2.x-1, k2.y-1, k2.name, color = 'white')
# ax.text(b1.x-1, b1.y-1, b1.name, color = 'white')
# ax.text(b2.x-1, b2.y-1, b2.name, color = 'white')
# ax.text(q.x-1, q.y-1, q.name, color = 'white')
# ax.text(p9.x-1, p9.y-1, p9.name, color = 'black')
# ax.text(p10.x-1, p10.y-1, p10.name, color = 'black')
# ax.text(p11.x-1, p11.y-1, p11.name, color = 'black')
# ax.text(p12.x-1, p12.y-1, p12.name, color = 'black')
# ax.text(p13.x-1, p13.y-1, p13.name, color = 'black')
# ax.text(p14.x-1, p14.y-1, p14.name, color = 'black')
# ax.text(p15.x-1, p15.y-1, p15.name, color = 'black')
# ax.text(p16.x-1, p16.y-1, p16.name, color = 'black')
# ax.text(r3.x-1, r3.y-1, r3.name, color = 'black')
# ax.text(r4.x-1, r4.y-1, r4.name, color = 'black')
# ax.text(k3.x-1, k3.y-1, k3.name, color = 'black')
# ax.text(k4.x-1, k4.y-1, k4.name, color = 'black')
# ax.text(b3.x-1, b3.y-1, b3.name, color = 'black')
# ax.text(b4.x-1, b4.y-1, b4.name, color = 'black')
# ax.text(kk.x-1, kk.y-1, kk.name, color = 'black')
# ax.text(qq.x-1, qq.y-1, qq.name, color = 'black')


plt.show()
while True:
    figure_name = input('введите название фигуры: ')
    for figure in all_figures:
        if figure_name == figure.name:
            a, b = map(int, input('введите координаты хода через пробел: ').split())
            figure.move(a, b)

    fig, ax = plt.subplots()
    ax.pcolormesh(board)
    for x in all_figures:
         ax.text(x.x - 1, x.y - 1, x.name)
    plt.show()
