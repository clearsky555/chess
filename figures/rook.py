from figures.figure import Figure, all_coords, all_figures


class Rook(Figure):
    def _check_rook_moves(self, x, y):
        if y - self.y < abs(8) and x == self.x or x - self.x < abs(8) and y == self.y:


            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x,y) and self._check_other_figures(x, y, None) and self._check_rook_moves(x,y):
            return True
        return False

    # def can_eat(self):
    #     for figure in all_figures:
    #         if [self.x, self.y] == [figure.x, figure.y]:
    #             for key, value in dict(all_coords).items():
    #                 if value == [figure.x, figure.y]:
    #                     del all_coords[key]
    #             all_figures.remove(figure)
    #             return True
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