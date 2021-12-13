from models.board_game import BoardGame
from models.manufacturer import Manufacturer

import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

board_game_repository.delete_all()
manufacturer_repository.delete_all()

mattel = Manufacturer("Mattel", "Contact Details")
manufacturer_repository.save(mattel)

scrabble = BoardGame("Scrabble", "A game", 1, 2, 2, mattel)
board_game_repository.save(scrabble)