from figures.king import King
from figures.pawn import Pawn
import numpy as np
import matplotlib.pyplot as plt

print('Это шахматный эмулятор')
p1 = Pawn(1,2,1)
p1.name = 'пешка1'
print(p1.__dict__)

p2 = Pawn(2,2,1)
p2.name = 'пешка2'

p3 = Pawn(3,2,1)
p3.name = 'пешка3'

p4 = Pawn(4,2,1)
p4.name = 'пешка4'

p5 = Pawn(5,2,1)
p5.name = 'пешка5'

p6 = Pawn(6,2,1)
p6.name = 'пешка6'

p7 = Pawn(7,2,1)
p7.name = 'пешка7'

p8 = Pawn(8,2,1)
p8.name = 'пешка8'

# p1.move(1,3)
k = King(1,1,1)
k.name = 'король'
# k.move(1,2)



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


ax.text(k.x-1, k.y-1, k.name, color = 'white')
ax.text(p1.x-1, p1.y-1, p1.name, color = 'white')
ax.text(p2.x-1, p2.y-1, p2.name, color = 'white')
ax.text(p3.x-1, p3.y-1, p3.name, color = 'white')
ax.text(p4.x-1, p4.y-1, p4.name, color = 'white')
ax.text(p5.x-1, p5.y-1, p5.name, color = 'white')
ax.text(p6.x-1, p6.y-1, p6.name, color = 'white')
ax.text(p7.x-1, p7.y-1, p7.name, color = 'white')
ax.text(p8.x-1, p8.y-1, p8.name, color = 'white')



plt.show()