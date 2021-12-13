import pdb
from models.board_game import BoardGame
import repositories.board_game_repository as board_game_repository

result = board_game_repository.select_all()

for board_game in result:
    print(board_game.__dict__)

pdb.set_trace()