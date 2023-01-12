from abc import ABC, abstractmethod
from enum import Enum

all_figures = []
class Color(Enum):
    white = 1
    black = 2

class Figure(ABC):
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        all_figures.append(self)
    def _check_other_figures(self, x, y, board):
        for figure in all_figures:
            if [x, y] == [figure.x, figure.y] and self.color == figure.color and self != figure:
                print('на этом месте стоит ваша фигура')
                return False
        return True

    def _check_borders(self, x, y):
        if x > 8 or x < 1 or y > 8 or y < 1:
            return False
        return True


    @abstractmethod
    def move(self, x, y):
        pass