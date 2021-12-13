from models.board_game import BoardGame
from models.manufacturer import Manufacturer

import repositories.board_game_repository as board_game_repository
import repositories.manufacturer_repository as manufacturer_repository

board_game_repository.delete_all()
manufacturer_repository.delete_all()

# MANUFACTURERS:

mattel = Manufacturer("Mattel", "Contact Details")
manufacturer_repository.save(mattel)

hasbro = Manufacturer("Hasbro", "Contact Details")
manufacturer_repository.save(hasbro)

days_of_wonder = Manufacturer("Days of Wonder", "Contact Details")
manufacturer_repository.save(days_of_wonder)

czech_games = Manufacturer("Czech Games Edition", "Contact Details")
manufacturer_repository.save(czech_games)

# BOARD GAMES:

scrabble = BoardGame("Scrabble", "A game", 5, 2, 2, mattel)
board_game_repository.save(scrabble)

monopoly = BoardGame("Monopoly", "A game", 4, 2, 2, hasbro)
board_game_repository.save(monopoly)

cluedo = BoardGame("Cluedo", "A game", 0, 2, 2, hasbro)
board_game_repository.save(cluedo)

ticket_to_ride = BoardGame("Ticket to Ride", "A game", 10, 2, 2, days_of_wonder)
board_game_repository.save(ticket_to_ride)

codenames = BoardGame("Codenames", "A game", 1, 2, 2, czech_games)
board_game_repository.save(codenames)
