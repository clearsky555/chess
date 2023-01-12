from figures.figure import Figure, all_figures


class Knight(Figure):
    def _check_knight_moves(self, x, y):
        if abs(y - self.y) == 2 and abs(x - self.x) == 1 or abs(x - self.x) == 2 and abs(y - self.y) == 1:
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_knight_moves(x,y):
            return True
        return False

    def move(self, x, y):
        if self._check(x, y):
            self.x = x
            self.y = y
            for figure in all_figures:
                if [self.x, self.y] == [figure.x, figure.y] and self.color != figure.color:

                    all_figures.remove(figure)
        else:
            print('move is invalid')
