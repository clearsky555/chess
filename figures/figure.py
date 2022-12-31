from abc import ABC, abstractmethod
from enum import Enum

all_coords = {}
all_figures = []
class Color(Enum):
    white = 1
    black = 2

class Figure(ABC):
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        # if self.color == 1:
        #     self.color = 'white'
        # else:
        #     self.color = 'black'
        self.name = name
        all_coords[name] = [self.x, self.y]
        all_figures.append(self)
    def _check_other_figures(self, x, y, board):
        return True

    def _check_borders(self, x, y):
        if x > 8 or x < 1 or y > 8 or y < 1:
            return False
        return True


    @abstractmethod
    def move(self, x, y):
        pass