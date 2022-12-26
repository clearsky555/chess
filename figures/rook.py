from figures.figure import Figure


class Rook(Figure):
    def _check_rook_moves(self, x, y):
        if y - self.y < abs(8) and x == self.x or x - self.x < abs(8) and y == self.y:
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_rook_moves(x,y):
            return True
        return False

    def move(self, x, y):
        if self._check(x, y):
            self.x = x
            self.y = y
        else:
            print('move is invalid')