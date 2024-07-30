from entities.game import Game
from system_design.tic_tac_game.entities.grid import Grid
from entities.player import Player

if __name__=='__main__':
    grid = Grid(3,3)
    game = Game(grid)


    num_players = int(input("How many players ? "))
    for i in range(num_players):
        player = Player(input(f'Enter name of Player {i+1}: '))
        game.add_player(player)

    game.start()
    

