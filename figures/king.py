from figures.figure import Figure


class King(Figure):
    def _check_king_moves(self, x, y):
        if y - self.y == abs(1) and x == self.x or x - self.x == abs(1) and y == self.y or abs(y - self.y) == abs(x - self.x) == 1:
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_king_moves(x,y):
            return True
        return False

    def move(self, x, y):
        if self._check(x, y):
            self.x = x
            self.y = y
        else:
            print('move is invalid')
