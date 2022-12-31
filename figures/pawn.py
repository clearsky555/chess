from figures.figure import Figure, all_coords, all_figures


class Pawn(Figure):
    def _check_pawn_moves(self, x, y):
        if y - self.y == 1 and x == self.x and self.color == 1 or y - self.y == -1 and x == self.x and self.color == 2:
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_pawn_moves(x,y):
            return True
        return False
    def can_eat(self):
        for figure in all_figures:
            if [self.x + 1, self.y + 1] == [figure.x, figure.y] and self.color == 1 or [self.x - 1, self.y + 1] == [figure.x, figure.y] and self.color == 1 or [self.x - 1, self.y - 1] == [figure.x, figure.y] and self.color == 2 or [self.x + 1, self.y - 1] == [figure.x, figure.y] and self.color == 2:
                all_figures.remove(figure)
                return True


    def move(self, x, y):
        if self._check(x, y) or self.can_eat():
            self.x = x
            self.y = y
            all_coords[self.name] = [self.x, self.y]

        else:
            print('move is invalid')