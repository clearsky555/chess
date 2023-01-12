from figures.figure import Figure, all_figures



class Pawn(Figure):
    def first_move(self):
        return True
    def _check_pawn_moves(self, x, y):
        if self.first_move:
            if abs(y - self.y) == 2 and x == self.x:
                return True
        if y - self.y == 1 and x == self.x and self.color == 1 or y - self.y == -1 and x == self.x and self.color == 2:
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_pawn_moves(x,y):
            return True
        return False

    def can_eat(self):

        for figure in all_figures:
            if abs(figure.x - self.x) == 1 and figure.y - self.y == 1 and self.color == 1:

                return True

            elif abs(figure.x - self.x) == 1 and figure.y - self.y == -1 and self.color == 2:

                return True




    def move(self, x, y):
        if self._check(x, y) or self.can_eat():
            self.x = x
            self.y = y
            for figure in all_figures:
                if [self.x, self.y] == [figure.x, figure.y] and self.color != figure.color:
                    all_figures.remove(figure)
            self.first_move = False

        else:
            print('move is invalid')