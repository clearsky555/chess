from figures.king import King
from figures.pawn import Pawn

print('Это шахматный эмулятор')
# p = Pawn(1,2,1)
# print(p.__dict__)
# p.move(1,3)
k = King(1,1,1)
k.move(1,2)

import numpy as np
import matplotlib.pyplot as plt

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


ax.text(0, 0, k, color = 'w')
ax.text(1, 1, 'pawn', color = 'w')
plt.show()