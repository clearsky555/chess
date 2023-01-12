from figures.figure import Figure, all_figures


class Bishop(Figure):
    def _check_bishop_moves(self, x, y):
        if abs(y - self.y) == abs(x - self.x):
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_bishop_moves(x,y):
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
