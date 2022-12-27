from figures.figure import Color
from figures.pawn import Pawn


class Game:
    def _init_figures(self):
        answer = []
        for i in range(1,9):
            answer.append(Pawn(i,2,color=Color.white))


        return []
    def __init__(self):
        self.figures = []
        self.is_black_did_castling = False
        self.is_white_did_castling = False
        self.move_counter = 0
        self.move_color = Color.white
        self.has_check = False
        self.has_mate = False

    def show(self):
        pass

print(answer)