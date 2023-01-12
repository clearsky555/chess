from figures.figure import Figure, all_figures


class King(Figure):
    def _check_king_moves(self, x, y):
        if abs(y - self.y) == 1 and x == self.x or abs(x - self.x) == 1 and y == self.y or abs(y - self.y) == abs(x - self.x) == 1:
            return True
        return False
    def first_move(self):
        return True

    def castling(self, rook):
        if self.first_move:
            if rook.x == 1 and rook.y == 1:
                rook.move(4,1)
                self.move(3,1)
            elif rook.x == 8 and rook.y == 1:
                rook.move(6,1)
                self.move(7,1)
            elif rook.x == 1 and rook.y == 8:
                rook.move(4,8)
                self.move(3,8)
            elif rook.x == 8 and rook.y == 8:
                rook.move(6,8)
                self.move(7,8)


    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_king_moves(x,y):
            return True
        return False

    def move(self, x, y):
        if self._check(x, y) or self.castling:
            self.x = x
            self.y = y
            for figure in all_figures:
                if [self.x, self.y] == [figure.x, figure.y] and self.color != figure.color:

                    all_figures.remove(figure)
            self.first_move = False
        else:
            print('move is invalid')
