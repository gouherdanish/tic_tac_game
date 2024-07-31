from entities.game import Game
from entities.grid import Grid
from entities.player import Player
from entities.entity_type import EntityType

if __name__=='__main__':
    grid = Grid(3,3)
    game = Game(grid)

    num_players = int(input("How many players ? "))
    for i in range(num_players):
        name = input(f'Enter name of Player {i+1}: ')
        player = Player(name)
        player.set_entity(EntityType.ENTITIES[i])
        game.add_player(player)

    game.start()
    

