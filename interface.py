from figures.figure import Color
from game import Game


def show_menu():
    print('1. начать новую игру')
    command = int(input())
    if command == 1:
        game = Game()
        while True:
            game.show()
            print('введите ваш ход')
            move = input()
            pass
            if game.has_mate:
                if game.move_color == Color.white:
                    winner = 'Белые'
                else:
                    winner = 'Черные'
                print(f'игра закончена, победили {winner}')

    else:
        print('неверная команда')