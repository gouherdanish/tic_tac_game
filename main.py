from entities.game import Game
from entities.grid import Grid
from entities.player import Player
from entities.entity_type import EntityType

if __name__=='__main__':
    nrows, ncols = map(int,input('Grid Dimesions ? ').split(' '))
    grid = Grid(nrows,ncols)
    game = Game(grid)

    num_players = int(input("How many players ? "))
    for i in range(num_players):
        name = input(f'Enter name of Player {i+1}: ')
        entity = EntityType.ENTITIES[i]
        player = Player(name,entity)
        game.add_player(player)

    game.start()
    

