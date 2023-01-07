from figures.figure import Figure, all_figures, all_coords


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
                    for key, value in dict(all_coords).items():
                        if value == [figure.x, figure.y]:
                            del all_coords[key]
                    all_figures.remove(figure)
            all_coords[self.name] = [self.x, self.y]
        else:
            print('move is invalid')
