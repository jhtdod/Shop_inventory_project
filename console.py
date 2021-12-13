from models.board_game import BoardGame
from models.manufacturer import Manufacturer

import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

result = board_game_repository.select_all()

for board_game in result:
    print(board_game.__dict__)